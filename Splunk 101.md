---
This room will cover the basics of Splunk.
---

# Splunk 101 — Writeup

## Overview
### Splunk 101 — Writeup
### Splunk 101 — Writeup
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-room-banner.png)
### Introduction to Splunk
Typically when people think of a SIEM Security Information and Event Management system that is used to aggregate security information in the form of logs, alerts, artifacts and events into a centralized platform that would allow security analysts to perform near real-time analysis during security monitoring.
they think of Splunk, and rightly so. Per the Splunk website, they boast that 91 of the Fortune 100 use Splunk.
Splunk is not only used for security; it's used for data analysis, DevOps, etc. But before speaking more on Splunk, what is a SIEM exactly?
A SIEM (Security Information and Event Management) is a software solution that provides a central location to collect log data from multiple sources within your environment. This data is aggregated and normalized, which can then be queried by an analyst.
As stated by [Varonis](https://www.varonis.com/blog/what-is-siem), there are 3 critical capabilities for a SIEM:
Threat detection
Investigation
Time to respond
Some other SIEM features:
Basic security monitoring
Advanced threat detection
Forensics & incident response
Log collection
Normalization
Notifications and alerts
Security incident detection
Threat response workflow
This room is a general overview of Splunk and its core features. Having experience with Splunk will help your resume stick out from the rest.
Splunk was named a "Leader" in [Gartner's](https://www.splunk.com/en_us/form/gartner-siem-magic-quadrant.html) 2020 Magic Quadrant for Security Information and Event Management.
Per Gartner, "Thousands of organizations around the world use Splunk as their SIEM for security monitoring, advanced threat detection, incident investigation and forensics, incident response, SOC automation and a wide range of security analytics and operations use cases."
Room Machine
Before moving forward, deploy the machine. If you want to RDP into the machine yourself:
Machine IP: 10.10.205.242
User name: administrator
User password: letmein123!
Open Chrome and navigate to the Splunk instance (http://127.0.0.1:8000). You may need to refresh the page until Splunk loads.
Note: Splunk can take up to five minutes to fully load.
If you want to install Splunk on your own machine, follow Splunk's official installation notes [here](Per Gartner, "Thousands of organizations around the world use Splunk as their SIEM for security monitoring, advanced threat detection, incident investigation and forensics, incident response, SOC automation and a wide range of security analytics and operations use cases."
Room Machine
Before moving forward, deploy the machine. If you want to RDP into the machine yourself:
Machine IP: 10.10.205.242
User name: administrator
User password: letmein123!
Open Chrome and navigate to the Splunk instance (http://127.0.0.1:8000). You may need to refresh the page until Splunk loads.
Note: Splunk can take up to five minutes to fully load.
If you want to install Splunk on your own machine, follow Splunk's official installation notes [here](https://docs.splunk.com/Documentation/Splunk/8.1.2/SearchTutorial/InstallSplunk).
Virtual machine deployed. *No answer needed*
### Navigating Splunk
When you access Splunk, you will see the default home screen identical to the screenshot below.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-home-screen.png)
Let's look at each section, or panel, that makes up the home screen. The top panel is the Splunk Bar (below image).
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-bar.png)
In the Splunk Bar, you can see system-level messages (Messages), configure the Splunk instance (Settings), review the progress of jobs (Activity), miscellaneous information such as tutorials (Help), and a search feature (Find).
The ability to switch between installed Splunk apps instead of using the Apps panel can be achieved from the Splunk Bar, like in the image below.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-bar2.png)
Next is the Apps Panel.  In this panel, you can see the apps installed for the Splunk instance.
The default app for every Splunk installation is Search & Reporting.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-apps-panel.png)
The next section is Explore Splunk. This panel contains quick links to add data to the Splunk instance, add new Splunk apps, and access the Splunk documentation.
![](https://assets.tryhackme.com/additional/splunk-overview/explore-splunk.png)
The last section is the Home Dashboard. By default, no dashboards are displayed. You can choose from a range of dashboards readily available within your Splunk instance. You can select a dashboard from the dropdown menu or by visiting the dashboards listing page.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-add-dashboard.gif)
You can also create dashboards and add them to the Home Dashboard. The dashboards you create can be viewed isolated from the other dashboards by clicking on the Yours tab.
Please review the Splunk documentation on Navigating Splunk [here](https://docs.splunk.com/Documentation/Splunk/8.1.2/SearchTutorial/NavigatingSplunk).
In the next section, we'll look at Splunk Apps a bit further.
I'm ready to look at Splunk apps.
*No answer needed*
### Splunk Apps
As mentioned in the previous task, Search & Reporting is a Splunk app installed by default with your Splunk instance. This app is also referred to as the Search app. If you click on the Search & Reporting app, you will be redirected to the Search app (see image below).
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-search.png)
The Search app is where you will enter your Splunk queries to search through the data ingested by Splunk. More on Splunk queries later.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-app-navigation.png)
The above image is the navigation for the Search app. Each app will have its own navigation menu. This menu is different from the menu/navigation within the Splunk bar, accessible throughout your entire Splunk session.
Let's draw our attention back to the Splunk Home page. In the Apps panel, there is a cog icon. By clicking the cog, you will be redirected to the Manage Apps page. From this page, you can change various settings (properties) for the installed apps. Let's look at the properties for the Search & Reporting app by clicking on Edit properties.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-app-properties.png)
You can change the app's display name, whether the app should check for updates, and whether the app should be visible in the Apps panel or not.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-app-properties2.png)
Tip: If you want to land into the Search app upon login automatically, you can do so by editing the user-prefs.conf file.
Windows: C:\Program Files\Splunk\etc\apps\user-prefs\default\user-prefs.conf
Linux: /opt/splunk/etc/apps/user-pref/default/user-prefs.conf
Before:
![](https://assets.tryhackme.com/additional/splunk-overview/user-prefs1.png)
After:
![](https://assets.tryhackme.com/additional/splunk-overview/user-prefs2.png)
Note: The above paths' base location will be different if you changed your Splunk install location.
Tip: Best practice is for any modifications to Splunk confs, you should create a directory and place custom conf settings there. When Splunk is upgraded the defaults are overwritten. For this room editing the defaults is OK.
In order for the user preferences changes to take effect, the splunkd service has to be restarted from a command-line prompt, using the following two commands: net stop splunkd and net start splunkd.
Lastly, you can install more Splunk apps to the Splunk instance to further expand Splunk's capabilities. You can either click on + Find More Apps in the Apps panel or Splunk Apps in the Explore Splunk panel.
![](https://assets.tryhackme.com/additional/splunk-overview/more-splunk-apps.png)
To install apps into the Splunk instance, you can either install directly from within Splunk or download it from Splunkbase and manually upload it to add it to your Splunk instance.
Note: You must have an account on Splunk.com to download and install Splunk apps.
If you wish to install the app manually, click the Install app from file button.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-install-app.png)
Just browse to the location of the app and upload it.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-install-app2.png)
You can also download the app (tgz file) from Splunkbase. You then unzip the file and place the entire directory into the Apps location for your Splunk instance.
Note: If you performed the install steps from the Linux section within this room and manually copied an App to the Apps location for your Splunk instance, you might need to change the file ownership and group to splunk or else your Splunk instance might not restart properly.
Back to Windows, if you wish to remove an app (or an add-on), you can do so via the command-line.
Below is the command to perform this task on Windows.
`C:\Program Files\Splunk\bin>splunk.exe remove app app-name -auth splunk-username:splunk-password`
Note: The syntax is similar on Linux machines.
If the command were successful, you would see the following output: App 'app-name' removed
Refer to the following Splunk documentation here for more information about managing Splunk apps.
Now time to upload an add-on into the Splunk instance.
There is a Splunk add-on on the desktop. Upload this add-on into the Splunk instance. Restart Splunk when prompted to.
![[Pasted image 20220906103524.png]]
![[Pasted image 20220906103429.png]]
What is the 'Folder name' for the add-on?
*TA-microsoft-sysmon* (after upload .gz)
What is the Version?
*10.6.2*
### Adding Data
Splunk can ingest any data. As per the Splunk documentation, when data is added to Splunk, the data is processed and transformed into a series of individual events.
The sources of the data can be event logs, website logs, firewall logs, etc.
Data sources are grouped into categories. Below is a chart listing from the Splunk documentation detailing each data source category.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-data-sources.png)
Please refer to the Splunk documentation here for more information regarding the specific data source you want to add Splunk.
In this room, we're going to focus on Sysmon Logs.
When we click on the Add Data link (from the Splunk home screen), we're presented with the following screen.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-add-data.png)
Looking at the guides, if we click on Operating System, we should see Windows event logs. But the only option available is Forward data to Splunk indexers. This is not what we want.
Let's ignore the guides and look at the bottom options: Upload, Monitor, and Forward.
Note: The above screenshot is what you'll see if you installed Splunk locally on your end. The Splunk instance in the attached room will only show Upload, Monitor, and Forward. (see below)
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-add-data-2.png)
Since we want to look at Windows event logs and Sysmon logs from this host system, we want Monitor.
There are many options to pick from on the following screen. Local Event Logs is the one we want.
![](https://assets.tryhackme.com/additional/splunk-overview/local-event-logs1.png)
Look at the list of Available item(s). Do you see PowerShell logs listed? How about Sysmon? I didn't either.
Another way we can add data to the Splunk instance is from Settings > Data Inputs.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-data-inputs.gif)
Upload the Splunk tutorial data on the desktop. How many events are in this source?
Note: Make sure you upload the data once only.
As you can see, there are A LOT more logs we can add to the Splunk instance.
Now it's your turn to add some data to the Splunk instance so we can start querying them.
![[Pasted image 20220906105105.png]]
*109,864* (upload tutorial.zip and choose segment value 1 next next and search)
### Splunk Queries
By now, you should have installed the Splunk app/add-on and added a data source to Splunk.
Now is the fun part, querying the data that is now residing in Splunk.
If you have completed the Windows Event Log and Sysmon rooms, you can remember that you queried the various logs using either Event Viewer, the command-line, or PowerShell and used filtering techniques to narrow down the information we're looking for.
Thankfully, with a SIEM (such as Splunk), we can create queries to find the data we're looking for across various data sources in one tool.
Enter an asterisk * in the Search bar and change the timeframe to search from Last 24 hours to All time. This will retrieve all the historical data within Splunk.
Even though we haven't discussed Filters yet but essentially Last 24 hours and All time are filters. We're instructing Splunk to output all the events from the historical data within the last 24 hours from the point in time we submit our query.
Click on the magnifying glass to initiate the search.
Note: The output you see might be different for you.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-search-results-new.png)
If you want to focus on a specific source or sourcetype, you can specify that within the Search bar. (see below image)
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-search-sources-new.png)
This information is also available if you click on source or sourcetype under Selected Fields.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-sourcetype-new.png)
Let's look at source.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-source-count-new.png)
From the above image, we see the names (values) of each source and the number of events (count), and the percentage value (%) of all the events for each source.
In the above image, the top 10 values are visible.
Let's start our query with Sysmon as the source. The query will look like this:
source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
We'll use this one, instead of WinEventLog:Microsoft-Windows-Sysmon/Operational, since it has more events we can sift through.
I'll select the first event that appeared for me for demonstration purposes. Expanding on the event, the details of the event are more readable.
Before:
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-sysmon-1.png)
After:
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-sysmon-2.png)
Some of these fields are specific to Sysmon. Refer to the Sysmon room if you are not familiar with Sysmon Event IDs.
Note: The fields will be different depending on the source/sourcetype.
