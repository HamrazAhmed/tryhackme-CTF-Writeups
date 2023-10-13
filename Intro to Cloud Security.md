# Intro to Cloud Security — Writeup

## Overview
### Intro to Cloud Security — Writeup
### Intro to Cloud Security — Writeup
----
Learn fundamental concepts regarding securing a cloud environment.
---
![](https://assets.tryhackme.com/room-banners/intro-to-offensive-security.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/2d08277a6c26c5d0976de96d0448ea28.png)
### Introduction
﻿Cloud computing is one of the IT industry's most common and evolving terms. In simple terms, it means delivering computing services over the internet. The customer does not need to buy and maintain physical data centres and servers in cloud computing. Instead, all services can be used with **pay-as-you-go pricing** (pay as per the usage of the services) and on an as-needed basis (we can access services when needed).
Learning Objectives
-   Understanding cloud security models.
-   Security through policies & procedures.
-   Security through identity & access management.
-   Security through networking management.
-   Security through storage management.
Course Pre-requisites
Understanding of following topics is recommended before starting the course:
-   [HTTP Protocols & Servers](https://tryhackme.com/room/protocolsandservers).
-   [Principles of Security](https://tryhackme.com/room/principlesofsecurity).
Let's begin!
Answer the questions below
I am ready to get started.
Completed
### Architectural Concepts of Cloud
Characteristics of Cloud
A few years back, no one could even imagine that organisations would place their data and operations on a geographically miles away platform that unknown people would manage. However, cloud computing is becoming so popular that organisations of every type and size use it for different purposes, such as storing data, taking backups, disaster recovery and Business Continuity Operations (BCO). It is becoming popular due to the following characteristics:
-   **Scalability**: In cloud computing, organisations only buy resources at a time. Instead, they buy upon the need. Also, resources can be scaled up or down as per business needs and requirements.
-   **Simplicity**: Renowned cloud service providers believe in simple design & interface. Usually, the customer only needs to buy and use the cloud services with little configuration.
-   **Cost Effective**: Cloud computing allows us to pay for our services. The cost is reduced as a third party provides infrastructure and does not need to be purchased at once.
-   **Enhance Automation**: Cloud computing services require limited human administration, so companies can focus more on their goals without worrying about managing and maintaining systems.
Models of Cloud Computing
The following three cloud computing models are based on what the cloud provider offers and the needs of customers/organisations.
**Infrastructure as a Service (IaaS)**
In IaaS, infrastructure is provided by cloud providers. The customer has complete control of operating systems, services and applications.
-   Cloud Provider’s Responsibility: Maintaining and providing data centres with racks, machines, cables, and utilities.
-   Customer’s Responsibility: In this case, the customer manages logical resources like software and operating system.
**Platform as a Service (PaaS)**
It contains all services offered in IaaS with the addition of an operating system (the user manages that in IaaS).
-   Cloud Providers’ Responsibility: In Platform as a Service, a cloud provider offers infrastructure and platform. Customers can choose any platform as per their needs. The service provider is responsible for managing the infrastructure and platform.
-   Customer's Responsibility: Customers can install software as per their requirements.
**Software as a Service (SaaS)**
It includes every service that is being provided in IaaS and PaaS.
-   Cloud Providers’ Responsibility: In SaaS, everything is managed by the cloud provider, including infrastructure, OS and software.
-   Customer Responsibility: This model is used by customers who need more technical skills in managing things. They only pay and use the services without worrying about the underlying architecture.
Cloud Deployment Models
**Public Cloud**
In the public cloud, as the name suggests, resources provided by cloud providers are shared among multiple customers. **Organisation A** will use resources from the same hardware that offers services to any other organisation. For example, Microsoft Azure and Amazon Web Services (AWS) are examples of public clouds. However, they also offer Virtual Private Cloud (VPC) services.
**Private Cloud**
In the private cloud, customers will not share the underlying resources (hardware and software) as in the public cloud, and resources are dedicated to a single customer. **Organisation A** will get a Virtual machine hosted on a system specifically dedicated to a particular customer.
**Hybrid Cloud**
It is a combination of a public and private cloud. For example, **Organisation A** might want to use some private cloud resources (to host confidential data of the production system) but also want some public cloud (for testing of the applications/software) so that the production system does not crash during testing.
Important Terminologies
There are some essential terminologies of cloud computing that one needs to understand. Some of the concepts are defined below:
-   **Virtualisation:** Virtualisation is the primary technology used in cloud computing that allows sharing of instances of an application or resources among multiple customers or users simultaneously.
-   **Compute:** Defined as the processing power customers require to run their applications and systems for data processing and carry out different tasks. In cloud computing, customers can get computing power from a combination of virtual machines hosted in the cloud environment.
-   **Storage:** In cloud computing, we do not need to buy and maintain physical hard drives; instead, our data is stored in logical pools of physical storage on cloud provider premises, and we can scale up and scale down the resources as per needs.
-   **Networking:** As cloud computing is a system of computers/processes that are interconnected, maintaining a high-speed network connection is very important. The cloud provider is responsible for providing network connectivity to meet customer needs without disruption.
Answer the questions below
```text
Infrastructure as a Service (IaaS), Platform as a Service (PaaS), y Software as a Service (SaaS) son tres modelos de servicio en la nube que proporcionan diferentes niveles de acceso y control a los recursos informáticos.

-   IaaS se refiere a la provisión de infraestructura de TI a través de la nube, incluyendo servidores virtuales, almacenamiento, redes y otros recursos informáticos. Con IaaS, el usuario tiene control total sobre el sistema operativo, middleware y aplicaciones, mientras que el proveedor de la nube se encarga de la gestión de la infraestructura física y de la virtualización. Ejemplos de servicios de IaaS incluyen Amazon Web Services (AWS), Microsoft Azure, y Google Cloud Platform.
    
-   PaaS se refiere a la provisión de una plataforma de desarrollo de aplicaciones a través de la nube, que permite a los desarrolladores crear, probar y desplegar aplicaciones sin tener que preocuparse por la gestión de la infraestructura subyacente. Con PaaS, el proveedor de la nube se encarga de la gestión de la infraestructura, mientras que el usuario se centra en el desarrollo de aplicaciones. Ejemplos de servicios de PaaS incluyen Microsoft Azure App Service, Google App Engine, y Heroku.
    
-   SaaS se refiere a la provisión de aplicaciones de software a través de la nube, que son accesibles a través de un navegador web o una aplicación móvil. Con SaaS, el usuario no tiene que preocuparse por la gestión de la infraestructura o del software subyacente, ya que todo está gestionado por el proveedor de la nube. Ejemplos de servicios de SaaS incluyen Salesforce, Microsoft Office 365, y Google Workspace.
    

En resumen, IaaS ofrece acceso a recursos informáticos básicos, PaaS ofrece una plataforma para el desarrollo de aplicaciones, y SaaS ofrece aplicaciones de software completas.
```
In Infrastructure as a Service, what will be deployed by the vendor (Hardware or Software)?
*Hardware*
What is the type of cloud dedicated to a single customer called?
*Private*
### Cloud Security Concepts
View Site
To understand cloud security concepts, first, we need to know what we need to protect in the cloud. The simple answer is "**Data**". Data is an asset and can be anything and any piece of information that any customer or organisation has. Data must be categorised into different levels (as defined below) before sharing in cloud platforms so that appropriate controls can be applied to protect it from a security point of view. There are three main classes of data depending on their sensitivity:
-   **Confidential data:** Confidential data can be considered the most critical data any organisation can have. Confidential information/data, if exposed, can damage an organisation’s reputation and even includes personally identifiable information.
-   **Internal data:** Internal data is information that, if exposed, causes moderate risk or harm to the company.
-   **Public data:** Public data is any information included on (or intended for) the public. There is no consequence if public data is leaked because it’s already meant for use by everyone.
Cloud Data Lifecycle
In today’s world, organisations store and use large amounts of data, including critical and sensitive data of the customers. Data on the cloud should be managed through its lifecycle to ensure its secure usage in every phase.
**Major Steps**
Data life cycle means the sequence of steps a particular data goes through from its creation to its deletion phase.
Security Aspects in Cloud Data Lifecycle
Each phase of the cloud data lifecycle requires protection. Below are the cloud data lifecycle stages, security considerations and requirements.
**Create/Update**
The create phase is the initial phase of the data lifecycle. It includes the newly created data and data that is being freshly imported from other data sources. In this phase, the data owner should be defined, and categorisation or classification of data should be done. Security aspects and challenges in this phase are as below:
-   **Implementing SSL/TLS:** Secure communication through SSL/TLS should be implemented so that it will be difficult for the attacker to listen to data transferred between the customer and the cloud provider.
-   **Encryption:** Data should be encrypted so that if data is exposed, the attacker cannot read it without decrypting it.
-   **Secure connections:** Secure connections and paths should be established for the data transfer so that change of data breach is minimised (ensures data security in transit).
**Store**
Data is processed based on its form (structured or unstructured) and stored in a container generally known as a database. Security aspects at this stage are as below:
-   **Encryption:** Data should be encrypted to protect data at rest.
-   **Backup:** Backup should be taken to prevent data loss; if data is lost, it can be restored from the available backups.
**Use**
As we know, if data is encrypted, it must be decrypted to be used by the application. Security aspects include the following means:
-   **Secure connections:** Encrypted paths should be established before data transfer to ensure the confidentiality and integrity of data in transit.
-   **Secure platform:** A secure authentication mechanism should be used, protected from attacks and vulnerabilities.
-   **Restrict Permissions:** Data owners should set strict permissions to modify and process data from unauthorised persons.
-   **Secure Virtualisation:** There is the concept of virtualisation in cloud computing in which resources among users are shared. So cloud providers need to ensure that one customer's data should not visible to other customers.
**Share**
Share data within or outside the cloud infra; challenges include:
-   **Jurisdiction:** Regulatory mandates/restrictions of sharing data across specific locations/regions.
-   **Data Loss Prevention (DLP):** Data Loss Prevention (DLP) helps to detect and prevent data breaches or unwanted destruction of sensitive data. It contains sensitive data from being shared with unauthorised persons.
**Archive**
Long-term storage of data and applications; security aspects include:
-   **Encryption:** Data should be encrypted before storing in cloud premises
-   **Physical Security:** It demands that the storage servers are physically secured and prevented from unauthorised access through biometrics, CCTV, etc.
-   **Location:** Reflects a physical location where data will be stored. Environmental factors such as natural disasters, climate, etc., can pose risks and consider Jurisdictional aspects (local and national laws) are key factors at this stage.
-   **Backup Procedure:** How will data be recovered when required and How often full/incremental backups will be carried out?
**Destroy**
Data should be destroyed once of no use so that it cannot be misused by any user (intentional or unintentional). Crypto shredding is a process in which encrypted data is useless by destroying cryptographic keys (without keys, data cannot be decrypted).
Security Issues in the Cloud & its Solution
Despite the benefits of cloud computing, several security challenges must be addressed effectively. These challenges raise concerns about fundamental security properties such as confidentiality, integrity and availability. Significant issues are as defined below:
-   **Data confidentiality:** When the data is hosted in the cloud, its privacy is at risk. As users have no physical access to their data once it has been outsourced, they don’t know how the confidentiality of their data is being maintained. Cloud service providers can examine the data of the users without detection.
-   **Virtualisation issues:** It allows the resources to be shared among the users. We need a mechanism to ensure isolation and secure communication between VMs. Users are not isolated in a multitenant environment, so one user can examine the data of another user.
-   **Insecure interfaces and API:** Cloud services are managed by the customers with the help of software or APIs. So vulnerable software or API can be risky, and data or customer confidentiality and integrity are at risk.
-   **Malicious insiders:** Some malicious insiders can cause the data breach of other clients. Taking advantage of shared technology vulnerabilities, these insiders can leak the data of other users or exploit security weaknesses, thus causing security threats to the other customers on the cloud.
-   **Account or service hijacking:** Several methods can cause account or service hijacking. These include phishing frauds, vulnerability exploitation and password reuse among users.
-   **Access Control Mechanism (ACM):** In a cloud computing environment, users and cloud servers are not in the same domain. Enforcing efficient and reliable access to information is critical when data is outsourced to the cloud. An unauthorised person can gain access to the data due to a lack of access control rights.
Answer the questions below
What is the first phase in the cloud data lifecycle?
*Create*
Click the **View Site** button at the top of the task to launch the static site in split view. What is the flag after completing the exercise?
![[Pasted image 20230303160952.png]]
![[Pasted image 20230303161118.png]]
### Cloud Security Risks Concerning Deployment Models
This task will briefly discuss various cloud deployment models and their associated risks. Read along the following topics to get an understanding of various cloud models.
_Click to enlarge the image._
Private Cloud
As studied, a private cloud is an environment in which resources are dedicated to a single customer. These are suitable for customers that are more concerned about the security of their data. Associated risks are as under:
-   **Personnel threats**: This includes both unintentional and intentional threats. Customers have no control over the provider’s data centre and administrators. Any insider can cause damage to customers’ data (either intentionally or unintentionally).
-   **Natural disasters**: Private cloud is vulnerable to natural disasters.
-   **External attacks**: Multiple attacks, such as unauthorised access, Man-in-the-middle attacks, and Distributed Denial of Service, can compromise the user’s data.
Public Cloud
In the public cloud, resources among users are shared with the help of virtualisation technology. Some risks include:
-   **Vendor Lock-In**: The customer becomes a dependent service provider in the public Cloud. It becomes nearly impossible for the customer to move the data out of the cloud infra before the end of the contract term; thereby, the customer becomes the hostage of the provider.
-   **Threat of new entrants**: Your cloud provider may provide services to your competitor in the public cloud.
-   **Escalation of Privilege Authorised**: In the public cloud, users may try to acquire unauthorized permissions. A user who gains illicit administrative access may be able to gain control of devices that process other customers’ data.
Community Cloud
Computing & storage infrastructure is shared between a specific community or organisation members. Some risks include:
-   **Vulnerability**: In a community cloud, any node may have vulnerabilities, which can also cause intrusions on the other nodes. Also, in a community, cloud configuration management and baselines are almost impossible (and very difficult to enforce).
-   **Policy and administration**: It is challenging to enforce decisions and procedures in the community cloud, posing a severe challenge and threat.
Answer the questions below
In which cloud model does the customer become the hostage of cloud providers (vendor locked in)?
*Public*
Is it challenging to enforce specific business decisions and procedures in the community cloud (yea/nay)?
*yea*
### Security Through Access Management
Access management is an important feature that ensures that the “right people” should do the “right job” within the “right set of permissions”. Access management has a critical role in cloud security as data is stored over the internet, and due to a plethora of cyber-attacks, it is inherently insecure. In cloud computing, Access Management is implemented through the following measures:
-   **Create Identities**: Cloud infrastructure creates “digital identities” that can relate to a person, user, API or service. An entity is a set of properties that can be recorded.
-   **Authentication Factors**: Each identity is allocated with a specific set of characteristics unique to that particular identity and helps to distinguish it from other identities. If they are matched, then the essence of that user is confirmed. These characteristics are called “Authentication Factors”, which include: username, password, PIN, biometric, certificate, FaceID, etc.
-   **Roles**: Each identity has a specific role which defines the domain under which that particular identity functions.
In Amazon, Access Management is implemented through Identity & Access Management (IAM). IAM is considered the “heart of access management” services to configure & perform fine-grained control and access policies to AWS resources. It is a web service that enables Amazon users to grant access to various services & resources to different users.
Features of IAM
-   Give rights & permissions of resources in your amazon account to other people without sharing passwords, etc.
-   Grant role-based access to users based on their access rights.
-   Enable multi-factor authentication.
-   Enable and manage permissions and access policies across amazon accounts & resources.
IAM Important Terminologies
To understand IAM, we must be very clear about its important terminologies:
-   Resources: These are objects within a particular service; these include users, roles, groups & policies.
-   Identities: Represent certain users permitted and authorised to perform specific roles and actions.
