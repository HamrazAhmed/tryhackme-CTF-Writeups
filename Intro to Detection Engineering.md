# Intro to Detection Engineering — Writeup

## Overview
### Intro to Detection Engineering — Writeup
### Intro to Detection Engineering — Writeup
----
Introduce the concept of detection engineering and the frameworks used towards crafting effective threat detection strategies.
----
![](https://assets.tryhackme.com/room-banners/sigma.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/60bdb80c8eed32b8f58d825281fe6ba0.png)
Detection engineering is an important role and task for a security analyst. It involves developing processes that will guide you as an analyst to identify threats, detect them through rules and processes, and fine-tune the process as the landscape changes.
- Understand what Detection Engineering is.
- Understand the Detection Engineering Lifecycle.
- Identify various frameworks used in Detection Engineering.
Answer the questions below
Let's begin.
Completed
### Task 2  What is Detection Engineering?
### ﻿Detection Engineering
Cybersecurity is growing and evolving at a rapid rate, compounded by the progress made in technology. With this, adversary actions are also evolving, and cyber attacks are becoming so rampant and sophisticated that it is difficult to keep up with them. Additionally, security teams must develop and adapt to new mindsets and practices that will aid them in keeping up with adversaries. That’s where detection engineering comes in.
Detection engineering is the continuous process of building and operating threat intelligence analytics to identify potentially malicious activity or misconfigurations that may affect your environment. It requires a cultural shift with the alignment of all security teams and management to build effective threat-rich defence systems.
### Detection Types
Threat detection can be viewed from two perspectives, each comprising two categories: The first one, **Environment-based** detection, focuses on looking at changes in an environment based on configurations and baseline activities that have been defined. Within this detection, we have Configuration detection and Modelling.
In the second perspective,  **Threat-based** detection focuses on elements associated with an adversary’s activity, such as tactics, tools and artefacts that would identify their actions. Under this, we have Indicators and Threat Behaviour detections.
### Configuration Detection
Under this detection, we use current knowledge of the known environment and infrastructure to identify misalignments. Configurations can cross domains, including network, asset or identity.
Configuration detection has the following benefits and challenges:
|**Benefits**|**Challenges**|
|---|---|
|The easiest form of detection to create and maintain in static environments.|Difficult to maintain in dynamic environments.|
|Under perfect conditions and coverage, it detects all malicious activity.|Limited visibility reduces effectiveness.|
|Individuals with different expertise can execute the detection.|There’s an assumption of knowledge of the working infrastructure and configurations for effectiveness.|
|Easy to combine with other detections for forensics and response.|Frequent configuration changes can result in high false positives.|
### Modelling
Threat detection under this type is done by defining baseline operations and activities and recording any deviations that occur. The primary assumption of this approach is that malicious activity can be sufficiently identified from benign activity.
The approach involves building an asset or activity profile that includes baseline events, time and data threshold. An in-depth look into baselining shall be discussed in the next task.
Some of the benefits and challenges of this detection method include the following:
|**Benefits**|**Challenges**|
|---|---|
|Used to identify unknown adversary activities due to model changes and not threat characteristics.|Provides no context of threat activity during investigations.|
|Easy to maintain in very static environments.|Difficult to maintain in dynamic environments.|
||Limited visibility reduces effectiveness.|
||Assumes in-depth knowledge of the working infrastructure and configurations.|
||Potentially adds existing malicious activity into the model.|
### Indicator Detection
As a reminder, indicators are pieces of information that identify a state and context of an element or entity. There are both `good` indicators used to identify legitimate activities or resources, such as those used in whitelists, and `bad` indicators used for suspicious or malicious resources, such as in blacklists or malware IPs.
IOCs are commonly referenced and derived from investigations against malicious events. By observing threat activities and investigations, analysts can use identified indicators to craft detections and adapt them based on an adversary’s rate of change.
Some of the benefits and challenges of this detection method include the following:
|**Benefits**|**Challenges**|
|---|---|
|Fastest detection to create and deploy.|The value of detection depends on the adversary’s rate of change.|
|Indicators raise specific threat contexts.|Retroactive in nature, one needs to observe the indicator first.|
|Useful for enriching data sources and detections.|Limited to some indicators that can be processed at a time.|
|Practical for scoping environments post investigation of indicators.|Unknown indicator expiry or change timelines can lead to false detections.|
### Threat Behaviour Detection
Analysts will look at an adversary’s Tactics, Techniques and Procedures (TTPs) to conduct an attack, regardless of any specific indicators. This makes detection more scalable beyond indicators.
Through this detection, analysts can focus their efforts more efficiently on responding to the threat and mitigate against it instead of utilising time and resources to understand how and why alerts were triggered. Additionally, threat behaviour detection can be paired with established workflows and playbooks to provide best practices that can be followed during an investigation.
Some of the benefits and challenges of this detection method include the following:
|**Benefits**|**Challenges**|
|---|---|
|Withstands the adversary’s rate of change.|Due to the adversary’s complexities, lots of data is required to provide complete coverage.|
|Easy to tune and adapt to different environments.|Moderately difficult to make initial implementations due to baseline assessments.|
|Low rates of false positives.|Only detects similar threat behaviour based on the set analytic.|
|Integrates with defensive playbooks and automated remediation plans.|Modifications must be made if detections must be reused across industries.|
Combining these forms of detection results in more robust defence systems. For example, model-based detection can be strengthened with expert-led configuration detection to reduce the chances of having false positives throwing alerts.
### Detection as Code
Detection as Code (DaC) is a structured approach to writing detections by incorporating software engineering best practice principles. This means that detection engineers and analysts will handle detection processes and logic as code, offering scalability to address the rapidly changing environments and adversary capabilities.
DaC offers a code-driven workflow that creates fine-tuned detection processes that introduce critical elements found in Continuous Integration/Continuous Development (CI/CD) workflows. Some of these elements include:
- **Version Control:** Most SIEMs and EDR products lack the ability to track changes made to alerts and their definitions. By introducing version control, detection rules and processes can be quickly reviewed, tested and accounted for, enabling higher-quality detections.
- **Automation workflows:** By adopting a CI/CD workflow, detection testing can be automated and allow quick transition and production delivery.
With that, Detection as Code provides the following benefits:
- **Customisable and Flexible Detections:** Using a common language for detections, such as Sigma and YARA, offers an opportunity for DaC to be vendor-agnostic and be deployed across numerous SIEM, EDR, and XDR solutions.
- **Test-Driven Development:** Quality testing of detection code can ensure that blind spots and false positive tests are identified earlier in the process and promote detection efficacy. Additionally, this approach improves the quality of detections and ensures they are well documented.
- **Team collaborations:** Using the CI/CD workflows eliminates isolation between security teams and fosters collaboration through the coding process.
- **Code Reusability:** With detection patterns emerging over time, engineers can reuse code to perform similar functions across different detections, ensuring that the detection process moves on faster since there won’t be the need to start from the beginning.
Answer the questions below
Which detection type focuses on misalignments within the current infrastructure?
*Configuration*
Which detection approach involves building an asset or activity baseline profile for detection?
*Modelling*
Which type of detection integrates with defensive playbooks?
*Threat Behaviour*
### Task 3  Detection Engineering Methodologies
### Detection Gap Analysis
The first step involves looking at the environment and identifying key areas where organisations can improve threat detection. This process is also known as **threat modelling** and can be done in the following ways:
- **Reactive**: Assessing the most recent internal incident reports, taking note of the lessons learnt from the attacks and curving out missed areas of possible detection.
- **Proactive**: Using the ATT&CK framework and various threat intelligence sources to map out potential areas of attack and the various TTPs that an adversary against your environment may use.
Note: Threat modelling in this context differs from the detection type discussed in the previous task.
### Datasource Identification and Log Collection
With information about the relevant threat actors, TTPs and potential risks the organisation may face, sources of relevant data associated with the risks need to be identified. This will determine what logs are currently available that will aid in defining detections against the threats and know which ones are missing and which are necessary.
### Baseline Creation
Before using all the collected information about adversaries, their TTPs and any malicious behaviour, security analysts need to know what normal behaviour is and set their security baselines. This will be a rolling process and requires participation from all departments within an organisation.
Setting up security baselines involves identifying the different types of devices running within an organisation based on their operating system, services and functions. Security baselines can be grouped into two categories:
- **High-level:** This sets broad OS independent standards guided by a specified security policy.
- **Technical:** This consists of OS-based configuration standards outlining different system functions and the intended behaviours or activities. For example, technical baselines outline OS hardening policies, network activities, Identity and Access Management (IAM) policies, and application policies.
### Log Collection
Once the baselines and sources of internal data have been identified and prioritised, the collection of logs and metadata useful for threat detection should be done. Depending on the infrastructure setup, a centralised system may aggregate all logs using network sensors for network data and services such as Sysmon to collect host data.
### Rule Writing
Based on the infrastructure setup and SIEM services, detection rules will need to be written and tested against the data sources. Detection rules test for abnormal patterns against logged events. Network traffic would be assessed via Snort rules, while Yara rules would evaluate file data. Check out the [Snort](https://tryhackme.com/room/snort) and [Yara](https://tryhackme.com/room/yara) rooms for more.
As part of the Detection Engineering module, we shall look at [Sigma](https://tryhackme.com/room/sigma), a generic signature language used to write detection rules against log files.
### Deployment, Automation & Tuning
Tested detection rules must be put into production to be assessed in a live environment. Over time, the detections would need to be modified and updated to account for changes in attack vectors, patterns or environment. This improves the quality of detections and encourages viewing detection as an ongoing process.
Answer the questions below
Read the above.
Completed
### Task 4  Detection Engineering Frameworks 1
### MITRE’s ATT&CK and CAR Frameworks
MITRE is well-known for publishing identified CVEs that adversaries would look to exploit for their malicious activities. Additionally, MITRE provides knowledge-based access that security analysts can use to track tactics and techniques commonly used by malicious actors across different platforms such as Windows, macOS, Linux, and Mobile.
The [ATT&CK framework](https://attack.mitre.org/) helps map out adversarial actions based on the infrastructure in use for detection engineering. It guides what to look for, especially as part of the detection gap analysis phase.
The CAR ([Cyber Analytics Repository](https://car.mitre.org/)) knowledge base is used to detect adversary behaviours and prioritise them based on the ATT&CK framework.
Click to enlarge the image.
### Pyramid of Pain
This is a well-known framework in the industry and is mainly used to showcase the pain for the adversary; if the defenders detect their TTPs, then how difficult and/or costly it would be for the adversary to change their TTPs.
### Cyber Kill Chain
