# Digital Forensics Case B4DM755 — Writeup

## Overview
### Digital Forensics Case B4DM755 — Writeup
### Digital Forensics Case B4DM755 — Writeup
----
Acquire the critical skills of evidence preservation, disk imaging, and artefact analysis for use in court.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/f8cb3550ee90bd530a581ef5199348ac.png)
Disclaimer
This fictional scenario presents a narrative with invented names, characters, and events. It is not meant to suggest any connection or resemblance to actual individuals, locations, structures, or merchandise.
Building up on Intro to Digital Forensics
During [Intro to Digital Forensics](https://tryhackme.com/room/introdigitalforensics), we learned about the two types of investigations that either the public-sector or private-sector initiates, the digital forensic process, and some practical examples of how we can apply our newly acquired knowledge of digital forensics.
In this room, we will simulate an actual crime scenario whereby a court of law has authorised us to conduct a search on a specific person and analyse obtained artefacts and evidence.
Room Objectives
Learn about the following to build up the confidence of future Forensics Lab Analysts, DFIR First Responders, and Digital Forensics Investigators:
- Ensure proper Chain of Custody procedures for transport to the Forensics Laboratory.
- Use FTK Imager to acquire a forensic disk image and preserve digital artefacts and evidence.
- Analyse forensic artefacts received at the Forensics Laboratory for presentation during a trial in a court of law.
Room Prerequisites
Before starting with this room, we recommend you clear [Intro to Digital Forensics](https://tryhackme.com/room/introdigitalforensics) and [Introduction to Cryptography](https://tryhackme.com/room/cryptographyintro).
Answer the questions below
I'm ready to investigate the case.
Question Done
### Task 2  Case B4DM755: Details of the Crime
Case B4DM755 - Details
|   |   |
|---|---|
Scenario
As a **Forensics Lab Analyst**, you analyse the artefacts from crime scenes. Occasionally, the law enforcement agency you work for receives "intelligence reports" about different cases, and today is one such day. A trusted informant, who has connections to an international crime syndicate, contacted your supervisor about William S. McClean from Case #B4DM755.
The informant provided information about the suspect's whereabouts in Metro Manila, Philippines, which is currently at large, and a transaction that will happen today with a local gang member. They also knew the exact location of the meetup and that the suspect would have incriminating materials at the time.
The law enforcement agency prepared for the operation by obtaining proper search authority and assigning a **DFIR (Digital Forensics & Incident Response) First Responder** (i.e., you) to ensure the appropriate acquisition of **digital artefacts and evidence** for examination at the Forensics Lab, and eventually for use in litigation. The court issued a **search warrant** on the same day, allowing law enforcement officers to investigate the suspect and his place of residence based on the informant's tip.
**NOTE:** In an understaffed agency, one person may be assigned multiple roles, including acquisition and analysis, particularly for high-profile cases. This can help minimize evidence tampering, and ensure accountability as the chain of custody is mainly handled by a single individual (i.e., you).
Answer the questions below
What is your official role?
*Forensics Lab Analyst*
What role was assigned to you for this specific scenario?
*DFIR First Responder*
What do you have to gather?
*digital artefacts and evidence*
What document is needed before performing any legal search?
*search warrant*
### Task 3  Practical Application of the Digital Forensics Process
Forensic Acquisition Process for Digital Artefacts and Evidence
|   |   |
|---|---|
Process for Establishing Chain of Custody
|   |   |
|---|---|
Before, during, and after turnover, ensure that the artefacts and evidence are complete and the Field Operative and Forensics Lab Analyst verifies inventory. Any related Chain of Custody forms must be adequately filled-out to guarantee a transparent and untainted handover of artefacts and evidence.
Answer the questions below
Before imaging drives, what must we check them for?
*drive encryption*
What should be done to ensure and maintain the integrity of original files in the Chain of Custody?
*Hash and copy*
What must be done before sending obtained artefacts to the Forensics Laboratory?
*Bag, Seal, and Tag the obtained artefacts*
### Task 4  Case B4DM755: At the Scene of Crime
Scenario (continuation)
Unfortunately, law enforcement arrived late at the suspect's residence, where the transaction supposedly happened. Upon arrival, everyone appeared to have already left; there were indications of evidence eradication attempts, and a transaction between the nefarious elements had successfully occurred.
During a thorough search of the suspect's place, law enforcement officers discovered a _flash drive_ under the desk. A key chain with the initials **WSM** was attached to the flash drive, which the team believes belongs to the suspect. It may have been left behind accidentally in their haste to vacate the place.
As a DFIR First Responder accompanying the Field Operatives, you documented, labelled, and preserved the artefact found and completed the Chain of Custody form. You then transported the artefact to the Forensics Laboratory for further examination.
Answer the questions below
What is the only possible artefact found in the suspect's residence?
*flash drive*
Based on the scenario and the previous task, what should be done with that acquired suspect artefact?
Task 3 explains the guidelines for proper forensic acquisition.
*Taking an image*
What is the crucial aspect of the Chain of Custody that ensures individual accountability and guarantees a transparent and untainted transfer of artefacts and evidence?
Task 3 explains the critical aspects of the Chain of Custody.
*Ensure proper documentation*
### Task 5  Introduction to FTK Imager
Start Machine
Connecting to the machine
Start the virtual machine in split-screen view by clicking on the green **Start Machine** button on the upper right section of this task. If the VM is not visible, use the blue **Show Split View** button at the top-right of the page. Alternatively, you can connect to the VM via RDP using the credentials below if **Split View** does not work.
|   |   |
|---|---|
|**Username**|analyst|
|**Password**|DFIR321!|
|**IP**|MACHINE_IP|
**IMPORTANT:** The attached VM has a copy of the FTK Imager installation. **Proceed to work on the subsequent tasks, and experiment with FTK Imager through a case example.**
FTK Imager
|   |   |
|---|---|
**NOTE:** In a real-world scenario, a Forensics Lab Analyst will use a write-blocking device to mount the suspect drive / forensic artefact to prevent accidental tampering.
FTK Imager - User Interface (UI)
|   |
|---|
|FTK Imager includes vital UI components that are crucial to its functionality. These components are:<br><br>- **Evidence Tree Pane**: Displays a hierarchical view of the added evidence sources such as hard drives, flash drives, and forensic image files.<br>- **File List Pane:** Displays a list of files and folders contained in the selected directory from the Evidence Tree Pane.<br>- **Viewer Pane:** Displays the content of selected files in either the Evidence Tree Pane or the File List Pane.|
Working with FTK Imager
**OBJECTIVES:** Verify encryption, obtain a forensic disk image, and analyse the recovered artefact.
**IMPORTANT:** The VM contains an emulated flash drive,**"\\PHYSICALDRIVE2 - Microsoft Virtual Disk [1GB SCSI]"**, to replicate the scenario where a physical drive, connected to a write blocker, is attached to an actual machine for forensic analysis. The steps performed in this activity are practically the same as in real-world situations. The write-protected flash drive is automatically attached to the VM upon startup.
STEP 1: Detecting EFS Encryption with FTK Imager
**IMPORTANT:** The drive's file system must be NTFS to utilise EFS encryption. EFS encryption is not compatible with FAT32 or exFAT file systems.
A Forensics Lab Analyst can perform the following steps to detect the presence of EFS encryption on a physical drive:
1. Open **FTK Imager** and navigate to `File > Add Evidence Item`
2. Choose **Physical Drive** on the **Select Source** window, then click **Next**.
3. Choose **Microsoft Virtual Disk** (our virtual flash drive) on the **Select Drive** window, then click **Finish**.
4. Navigate and click `File > Detect EFS Encryption` to scan the drive and detect the presence of encryption.
5. A message box will indicate whether or not EFS encryption is on the attached drive.
Answer the questions below
```text
EFS stands for "Encrypting File System," and it is a feature in some operating systems that provides transparent encryption of files and folders on a storage device. When EFS is enabled for a file or folder, the data is encrypted before being written to disk and decrypted when accessed, providing an additional layer of security for sensitive data.

EFS encryption uses a combination of asymmetric and symmetric encryption. Each file or folder has an associated file encryption key (FEK), which is used for symmetric encryption. The FEK is then encrypted using the public key of the user who encrypted the file, and this encrypted FEK is stored in the file's metadata. When a user wants to access the encrypted file, their private key is used to decrypt the FEK, which is then used to decrypt the file's contents.

EFS encryption is a powerful security feature that helps protect data at rest. However, it's important to note that EFS only protects data on the storage device. Data in transit or while it is being processed in memory is not covered by EFS. Additionally, it's crucial to manage and protect the private keys used in the encryption process to ensure the overall security of the system.
```
Start the attached VM, work on the subsequent tasks, and experiment with FTK Imager through a case example.
Completed
What device will prevent tampering when acquiring a forensic disk image?
*write-blocking device*
What is the UI element of FTK Imager which displays a hierarchical view of the added evidence sources?
*Evidence Tree Pane*
Is the attached flash drive encrypted? (Y/N)
*N*
What is the UI element of FTK Imager which displays a list of files and folders?
*File List Pane*
### Task 6  Using FTK Imager to Acquire Digital Artefacts and Evidence
STEP 2: Creating a Forensic Disk Image with FTK Imager
A Forensics Lab Analyst can perform the following steps to create a forensic disk image from a physical drive:
1. Open **FTK Imager** and navigate to `File > Create Disk Image`
2. Choose **Physical Drive** on the **Select Source** window, then click **Next**.
3. Choose **Microsoft Virtual Disk** (our virtual flash drive) on the **Select Drive** window, then click **Finish**.
4. Ensure you check **"Verify images after they are created"** and **"Create directory listings of all files in the image after they are created"** on the **Create Image** window. Press **Add** to open the **Select Image Type** window, choose **Raw (dd)**, then click **Next**.
5. Enter case details in the **Evidence Item Information** window, then click **Next**.
6. Enter the **Image Destination Folder** and **Image Filename**, then click **Finish**.
7. Press **Start** to begin creating the _forensic disk image_.
8. When you check **"Verify images after they are created"**, FTK Imager will hash both the physical drive and the forensic disk image after disk imaging. It will then **validate if both hashes are equal to confirm a match**.
**Note:** You can go ahead and answer Question 1 and 2, then come back and follow along with the Step 3 section.
STEP 3: Mounting a Forensic Disk Image and Extracting Artefacts
A Forensics Lab Analyst can perform the following steps to mount a forensic disk image and extract artefacts using FTK Imager:
1. Open **FTK Imager** and navigate to `File > Add Evidence Item`
2. Choose **Image File** on the **Select Source** window, then click **Next**.
3. Set **Evidence Source** to the path of the forensic disk image that we created previously and click **Finish**.
4. The **Evidence Tree Pane** will be populated, and artefacts will be visible on the **File List Pane**. The **Viewer Pane** will display the contents of selected elements for analysis.
**IMPORTANT:** During forensic analysis with FTK Imager, it is always crucial to analyse using the forensic disk image that has been created. It is also equally important to look for signs of **deleted files (i.e., those with an x symbol)**, **corrupted files (e.g., 0 file size)** and **obfuscation (e.g., conflicting information about a file's extension and header information)**.
5. To recover all deleted files, right-click on the target directory or file and press **Export Files** to save artefacts.
Answer the questions below
What is the UI element of FTK Imager which displays the content of selected files?
*Viewer Pane*
What is the SHA1 hash of the physical drive and forensic image?
*d82f393a67c6fc87a023b50c785a7247ab1ac395*
Including hidden files, how many files are currently stored on the flash drive?
Use Windows Explorer and open the flash drive.
![[Pasted image 20230718134650.png]]
*8*
How many files were deleted in total?
The x Symbol might be hard to see; look closely in the File List Pane.
![[Pasted image 20230718134755.png]]
*6*
How many recovered files are corrupted (e.g., 0 file size)?
*3*
### Task 7  Case B4DM755: At the Forensics Laboratory
Scenario (continuation)
Upon receiving the artefacts and evidence from the crime scene at the Forensics Lab, it is imperative to establish their authenticity. Since the DFIR First Responders recovered only a flash drive, you then proceed with the following actions:
- Verify and document every detail of the Chain of Custody form from the crime scene to the present.
- Use FTK Imager to create a forensic disk image of the seized flash drive from the suspect's (William S. McClean) residence in Case B4DM755.
- Match the cryptographic hashes of the physical drive and the acquired forensic image to guarantee the authenticity and integrity of the artefacts, making them admissible evidence in a court of law.
- Preserve the physical evidence (i.e., flash drive) for presentation in a court of law during trial after creating a forensic disk image.
- Perform any review and analysis on the created forensic disk image to avoid tampering with evidence.
- Document all examination operations and activities to ensure the admissibility of evidence in court.
- During a presentation at trial, ensure that the cryptographic hashes of the physical evidence and the forensic disk image MATCH.
Answer the questions below
Aside from FTK Imager, what is the directory name of the other tool located in the tools directory under Desktop?
![[Pasted image 20230718135028.png]]
*exiftool-12.47*
What is the visible extension of the "hideout" file?
*.pdf*
View the metadata of the "hideout" file. What is its actual extension?
FTK Imager's Viewer Pane or exiftool can help.
```text
C:\Users\dfir>cd C:\tools\exiftool-12.47

C:\tools\exiftool-12.47>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\tools\exiftool-12.47

05/25/2023  02:23 PM    <DIR>          .
05/25/2023  02:23 PM    <DIR>          ..
10/04/2022  02:40 AM         8,903,384 exiftool.exe
               1 File(s)      8,903,384 bytes
               2 Dir(s)  27,171,061,760 bytes free

C:\tools\exiftool-12.47>exiftool.exe C:\Users\dfir\Desktop\artefacts\[root]\hideout.pdf
ExifTool Version Number         : 12.47
File Name                       : hideout.pdf
Directory                       : C:/Users/dfir/Desktop/artefacts/[root]
File Size                       : 4.7 MB
File Modification Date/Time     : 2022:09:11 04:31:48+00:00
File Access Date/Time           : 2023:03:31 21:02:26+00:00
File Creation Date/Time         : 2023:03:31 21:02:23+00:00
File Permissions                : -rw-rw-rw-
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
Make                            : OnePlus
Camera Model Name               : ONEPLUS A6013
Orientation                     : Horizontal (normal)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Modify Date                     : 2022:09:11 12:31:48
Y Cb Cr Positioning             : Centered
Exposure Time                   : 1/220
F Number                        : 1.7
Exposure Program                : Program AE
ISO                             : 100
Exif Version                    : 0220
Date/Time Original              : 2022:09:11 12:31:48
Create Date                     : 2022:09:11 12:31:48
Components Configuration        : Y, Cb, Cr, -
Shutter Speed Value             : 1/219
Aperture Value                  : 1.7
Brightness Value                : 2.87
Exposure Compensation           : 0
Max Aperture Value              : 1.7
Metering Mode                   : Multi-segment
Light Source                    : Unknown
Flash                           : Off, Did not fire
Focal Length                    : 4.3 mm
Sub Sec Time                    : 728794
Sub Sec Time Original           : 728794
Sub Sec Time Digitized          : 728794
Flashpix Version                : 0100
Color Space                     : sRGB
Exif Image Width                : 4608
Exif Image Height               : 3456
Interoperability Index          : R98 - DCF basic file (sRGB)
Interoperability Version        : 0100
Sensing Method                  : Not defined
Scene Type                      : Directly photographed
Exposure Mode                   : Auto
White Balance                   : Auto
Focal Length In 35mm Format     : 25 mm
Scene Capture Type              : Standard
Compression                     : JPEG (old-style)
Thumbnail Offset                : 900
Thumbnail Length                : 40889
XMP Toolkit                     : Adobe XMP Core 5.1.0-jc003
Capture Mode                    : Photo
Scene                           : AutoHDR
Is HDR Active                   : False
Is Night Mode Active            : False
Scene Detect Result Ids         : [60, 42]
Scene Detect Result Confidences : [0.99988556, 0.97189426]
Lens Facing                     : Back
Image Width                     : 4608
Image Height                    : 3456
Encoding Process                : Baseline DCT, Huffman coding
