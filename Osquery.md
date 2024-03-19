---
Learn how to use this operating system instrumentation framework to explore operating system data by using SQL queries.
---

# Osquery — Writeup

## Overview
### Osquery — Writeup
### Osquery — Writeup
![](https://assets.tryhackme.com/additional/osquery/osquery_room_banner2.png)
### Introduction
[Osquery](https://osquery.io/) is an [open-source](https://github.com/osquery/osquery) tool created by [Facebook](https://engineering.fb.com/2014/10/29/security/introducing-osquery/). With Osquery, Security Analysts, Incident Responders, Threat Hunters, etc., can query an endpoint (or multiple endpoints) using SQL syntax. Osquery can be installed on multiple platforms: Windows, Linux, macOS, and FreeBSD.
Many well-known companies, besides Facebook, either use Osquery, utilize osquery within their tools, and/or look for individuals who know Osquery.
As of today (March 2021), Github and AT&T seek individuals who have experience with Osquery.
Github:
![](https://assets.tryhackme.com/additional/osquery/github-posting.png)
AT&T:
![](https://assets.tryhackme.com/additional/osquery/att-posting.png)
Some of the tools (open-source and commercial) that utilize Osquery are listed below.
Alienvault: [The AlienVault agent](https://otx.alienvault.com/endpoint-security/welcome) is based on Osquery.
Cisco: Cisco AMP (Advanced Malware Protection) for endpoints utilize Osquery in [Cisco Orbital](https://orbital.amp.cisco.com/help/).
Learning Osquery will be beneficial if you are looking to enter into this field or if you're already in the field and you're looking to level up your skills.
Note: It is highly beneficial if you're already familiar with SQL queries. If not, check out this [SQL Tutorial](https://www.w3schools.com/sql/sql_intro.asp).
Ready to learn Osquery!
*No answer needed*
### Installation
The virtual machine attached to this room already has Osquery installed and configured for you on Windows and Linux.
Before proceeding start the attached VM.
Machine IP: MACHINE_IP
Username: administrator
Password: letmein123!
If you wish to install Osquery on your local machine or local virtual machine, please refer to the installation instructions.
[Install on Windows](https://osquery.readthedocs.io/en/stable/installation/install-windows/)
[Install on Linux](https://osquery.readthedocs.io/en/stable/installation/install-linux/)
Install on macOS
Install on FreeBSD
Refer to the documentation on the Osquery daemon (osqueryd) information and all the command-line flags [here](https://osquery.readthedocs.io/en/latest/installation/cli-flags/).
Attached VM was started. Ready to proceed.
*No answer needed*
### Interacting with the Osquery Shell
To interact with the Osquery interactive console/shell, open CMD (or PowerShell) and run osqueryi.
As per the documentation, osqueryi is a modified version of the SQLite shell.
You'll know that you've successfully entered into the interactive shell by the new command prompt.
![](https://assets.tryhackme.com/additional/osquery/osquery_prompt.png)
One way to familiarize yourself with the Osquery interactive shell, as with any new tool, is to check its help menu.
In Osquery, the help command (or meta-command) is .help.
![](https://assets.tryhackme.com/additional/osquery/osquery_help.png)
Note: As per the documentation, meta-commands are prefixed with a '.'.
To list all the available tables that can be queried, use the .tables meta-command.
For example, if you wish to check what tables are associated with processes, you can use .tables process.
![](https://assets.tryhackme.com/additional/osquery/osquery_tables.png)
In the above image, 3 tables are returned that contain the word 'process.'
Note: Depending on the operating system, different tables will be returned when the .tables meta-command is executed.
Table names are not enough to know exactly what information is contained in any given table without actually querying it.
Knowing what columns and types, known as a schema, for each table are also useful.
You can list a table's schema with the following meta-command: .schema table_name
![](https://assets.tryhackme.com/additional/osquery/osquery_schema.png)
Looking at the above image, pid is the column, and BIGINT is the type.
Note: Any user on a system can run and interact with osqueryi, but some tables might return limited results compared to running osqueryi from an elevated shell.
If you which to check the schema for another operating system, you'll need to use the --enable_foreign command-line flag.
To read more about command-line flags, refer to this page, https://osquery.readthedocs.io/en/latest/installation/cli-flags/.
Interacting with the shell to get quick schema information for a table is good but not ideal when you want schema information for multiple tables.
For that, the schema API online documentation can be used to view a complete list of tables, columns, types, and column descriptions.
```text
osquery> .version
osquery 4.6.0.2
using SQLite 3.34.0
```
What is the Osquery version?
*4.6.0.2*
What is the SQLite version?
*3.34.0*
```text
osquery> .show
[1mosquery[0m - being built, with love.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
osquery 4.6.0.2
using SQLite 3.34.0

General settings:
     Flagfile:
       Config: filesystem (\Program Files\osquery\osquery.conf)
       Logger: filesystem (\Program Files\osquery\log\)
  Distributed: tls
     Database: ephemeral
   Extensions: core
       Socket: \\.\pipe\shell.em

Shell settings:
         echo: off
      headers: on
         mode: pretty
    nullvalue: ""
       output: stdout
    separator: "|"
        width:

Non-default flags/options:
  database_path: C:\Users\Administrator\.osquery\shell.db
  disable_database: true
  disable_events: true
  disable_logging: true
  disable_watchdog: true
  extensions_socket: \\.\pipe\shell.em
  hash_delay: 0
  logtostderr: true
  stderrthreshold: 0
```
What is the default output mode?
*pretty*
```text
osquery> .help
Welcome to the osquery shell. Please explore your OS!
You are connected to a transient 'in-memory' virtual database.

.all [TABLE]     Select all from a table
.bail ON|OFF     Stop after hitting an error
.echo ON|OFF     Turn command echo on or off
.exit            Exit this program
.features        List osquery's features and their statuses
.headers ON|OFF  Turn display of headers on or off
.help            Show this message
.mode MODE       Set output mode where MODE is one of:
                   csv      Comma-separated values
                   column   Left-aligned columns see .width
                   line     One value per line
                   list     Values delimited by .separator string
                   pretty   Pretty printed SQL results (default)
.nullvalue STR   Use STRING in place of NULL values
.print STR...    Print literal STRING
.quit            Exit this program
.schema [TABLE]  Show the CREATE statements
.separator STR   Change separator used by output mode
.socket          Show the osquery extensions socket path
.show            Show the current values for various settings
.summary         Alias for the show meta command
.tables [TABLE]  List names of tables
.types [SQL]     Show result of getQueryColumns for the given query
.width [NUM1]+   Set column widths for "column" mode
.timer ON|OFF      Turn the CPU timer measurement on or off
```
What is the meta-command to set the output to show one value per line?
*.mode line*
What are the 2 meta-commands to exit osqueryi?
*.quit,.exit*
### Schema Documentation
Head over to the schema documentation [here](https://osquery.io/schema/4.7.0/).
![](https://assets.tryhackme.com/additional/osquery/osquery_apischema-1.png)
The above image is a resemblance to what you'll see when you navigate to the page.
Note: At the time of this writing, the current version for Osquery is 4.7.0.
A breakdown of the information listed on the schema API page is explained below.
A dropdown listing various versions of Osquery. Choose the version of Osquery you wish to see schema tables for.
The number of tables within the selected version of Osquery. (In the above image, 271 tables exist for Osquery 4.7.0)
The list of the tables is listed in alphabetical order for the selected version of Osquery.
The name of the table and a brief description.
A detailed chart listing the column, type, and column description for each table.
Information to which operating system the table applies to. (In the above image, the account_policy_data table is available only for macOS)
You have enough information to confidently navigate this resource to retrieve any information you'll need.
![[Pasted image 20220905130039.png]]
What table would you query to get the version of Osquery installed on the Windows endpoint?
*osquery_info*
How many tables are there for this version of Osquery?
*266* (version 4.6.0)
How many of the tables for this version are compatible with Windows?
*96* (Show only Tables compatible with: Windows)
How many tables are compatible with Linux?
*155*
What is the first table listed that is compatible with both Linux and Windows?
*arp_cache* (Show only Tables compatible with: Windows,Linux)
### Creating queries
The SQL language implemented in Osquery is not an entire SQL language that you might be accustomed to, but rather it's a superset of SQLite's.
Realistically all your queries will start with a SELECT statement. This makes sense because, with Osquery, you are only querying information on an endpoint or endpoints. You won't be updating or deleting any information/data on the endpoint.
The exception to the rule: The use of other SQL statements, such as UPDATE and DELETE, is possible, but only if you're creating run-time tables (views) or using an extension if the extension supports them.
Your queries will also include a FROM clause and end with a semicolon.
If you wish to retrieve all the information about the running processes on the endpoint: `SELECT * FROM processes;`
![](https://assets.tryhackme.com/additional/osquery/osquery_selectall.png)
Note: The results for you will be different if you run this query in the attached VM or your local machine (if Osquery is installed).
The number of columns returned might be more than what you need. You can select specific columns rather than retrieving every column in the table.
Query: SELECT pid, name, path FROM processes;
![](https://assets.tryhackme.com/additional/osquery/osquery_notselectall.png)
```text
osquery> select pid, name, path from processes;
+------+--------------------------+---------------------------------------------------------------------------------+
| pid  | name                     | path                                                                            |
+------+--------------------------+---------------------------------------------------------------------------------+
| 0    | [System Process]         |                                                                                 |
| 4    | System                   |                                                                                 |
| 88   | Registry                 |                                                                                 |
| 432  | smss.exe                 | C:\Windows\System32\smss.exe                                                    |
| 592  | csrss.exe                |                                                                                 |
| 664  | csrss.exe                |                                                                                 |
| 684  | wininit.exe              | C:\Windows\System32\wininit.exe                                                 |
| 724  | winlogon.exe             | C:\Windows\System32\winlogon.exe                                                |
| 800  | services.exe             | C:\Windows\System32\services.exe                                                |
| 808  | lsass.exe                | C:\Windows\System32\lsass.exe                                                   |
| 924  | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 944  | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 964  | fontdrvhost.exe          |                                                                                 |
| 972  | fontdrvhost.exe          |                                                                                 |
| 8    | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 596  | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 796  | dwm.exe                  |                                                                                 |
| 1036 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1048 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1076 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1280 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1288 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1340 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1348 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1360 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1368 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1440 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1452 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1532 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1552 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1580 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1652 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1684 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1756 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1788 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1796 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1896 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1968 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2028 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1416 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2096 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2156 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2168 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2284 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2328 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2632 | spoolsv.exe              | C:\Windows\System32\spoolsv.exe                                                 |
| 2684 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2692 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2708 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2756 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2824 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2832 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2852 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2876 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2952 | LiteAgent.exe            | C:\Program Files\Amazon\Xentools\LiteAgent.exe                                  |
| 2980 | vm3dservice.exe          | C:\Windows\System32\vm3dservice.exe                                             |
| 3020 | vm3dservice.exe          | C:\Windows\System32\vm3dservice.exe                                             |
| 2220 | Sysmon.exe               | C:\Windows\Sysmon.exe                                                           |
| 2452 | MsMpEng.exe              | C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2103.7-0\MsMpEng.exe    |
| 2064 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2516 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 3760 | LogonUI.exe              | C:\Windows\System32\LogonUI.exe                                                 |
| 3956 | unsecapp.exe             |                                                                                 |
| 4276 | NisSrv.exe               | C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2103.7-0\NisSrv.exe     |
| 4820 | amazon-ssm-agent.exe     | C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe                                |
| 4912 | ssm-agent-worker.exe     | C:\Program Files\Amazon\SSM\ssm-agent-worker.exe                                |
| 4932 | conhost.exe              | C:\Windows\System32\conhost.exe                                                 |
| 4928 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1308 | GoogleUpdate.exe         | C:\Program Files (x86)\Google\Update\GoogleUpdate.exe                           |
| 1400 | msdtc.exe                | C:\Windows\System32\msdtc.exe                                                   |
| 1588 | GoogleCrashHandler.exe   | C:\Program Files (x86)\Google\Update\1.3.36.72\GoogleCrashHandler.exe           |
| 1592 | GoogleCrashHandler64.exe | C:\Program Files (x86)\Google\Update\1.3.36.72\GoogleCrashHandler64.exe         |
| 2648 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 4292 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 4100 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 4092 | csrss.exe                |                                                                                 |
| 3976 | winlogon.exe             | C:\Windows\System32\winlogon.exe                                                |
| 3708 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2860 | fontdrvhost.exe          |                                                                                 |
| 3196 | dwm.exe                  |                                                                                 |
| 2772 | rdpclip.exe              | C:\Windows\System32\rdpclip.exe                                                 |
| 4660 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2640 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 5080 | taskhostw.exe            | C:\Windows\System32\taskhostw.exe                                               |
| 3628 | sihost.exe               | C:\Windows\System32\sihost.exe                                                  |
| 3548 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1092 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 3100 | ctfmon.exe               | C:\Windows\System32\ctfmon.exe                                                  |
| 4636 | explorer.exe             | C:\Windows\explorer.exe                                                         |
| 4596 | ShellExperienceHost.exe  | C:\Windows\SystemApps\ShellExperienceHost_cw5n1h2txyewy\ShellExperienceHost.exe |
| 4564 | SearchUI.exe             | C:\Windows\SystemApps\Microsoft.Windows.Cortana_cw5n1h2txyewy\SearchUI.exe      |
| 4156 | RuntimeBroker.exe        | C:\Windows\System32\RuntimeBroker.exe                                           |
| 5224 | RuntimeBroker.exe        | C:\Windows\System32\RuntimeBroker.exe                                           |
| 5388 | RuntimeBroker.exe        | C:\Windows\System32\RuntimeBroker.exe                                           |
| 5680 | cmd.exe                  | C:\Windows\System32\cmd.exe                                                     |
| 5688 | conhost.exe              | C:\Windows\System32\conhost.exe                                                 |
| 5828 | osqueryi.exe             | C:\ProgramData\chocolatey\bin\osqueryi.exe                                      |
| 5880 | osqueryi.exe             | C:\ProgramData\chocolatey\lib\osquery\osqueryi.exe                              |
| 4592 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 2556 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 1384 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
| 4020 | WmiPrvSE.exe             |                                                                                 |
| 6088 | svchost.exe              | C:\Windows\System32\svchost.exe                                                 |
+------+--------------------------+---------------------------------------------------------------------------------+
```
The above query will list the process id, the process's name, and the path for all running processes on the endpoint.
This will still return a large number of results, depending on how busy the endpoint is.
The count() function can be used to get exactly how many.
Query: `SELECT count(*) from processes;`
![](https://assets.tryhackme.com/additional/osquery/osquery_count.png)
```text
osquery> select count(*) from processes;
+----------+
| count(*) |
+----------+
| 103      |
+----------+
```
The output can be limited to the first 3 in ascending order by process name, as shown below.
![](https://assets.tryhackme.com/additional/osquery/osquery_orderby_limit.png)
```text
osquery> select pid, name, path from processes order by name limit 3;
+------+--------------------------+-------------------------------------------------------------------------+
| pid  | name                     | path                                                                    |
+------+--------------------------+-------------------------------------------------------------------------+
| 1588 | GoogleCrashHandler.exe   | C:\Program Files (x86)\Google\Update\1.3.36.72\GoogleCrashHandler.exe   |
| 1592 | GoogleCrashHandler64.exe | C:\Program Files (x86)\Google\Update\1.3.36.72\GoogleCrashHandler64.exe |
| 1308 | GoogleUpdate.exe         | C:\Program Files (x86)\Google\Update\GoogleUpdate.exe                   |
+------+--------------------------+-------------------------------------------------------------------------+
```
Optionally, you can use a WHERE clause to narrow down the list of results returned based on specified criteria.
Query: `SELECT pid, name, path FROM processes WHERE name='lsass.exe';`
![](https://assets.tryhackme.com/additional/osquery/osquery_where.png)
```text
osquery> select pid, name, path from processes where name="lsass.exe";
+-----+-----------+-------------------------------+
| pid | name      | path                          |
+-----+-----------+-------------------------------+
| 808 | lsass.exe | C:\Windows\System32\lsass.exe |
+-----+-----------+-------------------------------+
```
The equal sign is not the only filtering option available in a WHERE clause.
Below are filtering operators that can be used in a WHERE clause:
= [equal]
<>  [not equal]
>, >= [greater than, greater than or equal to]
<, <= [less than or less than or equal to]
BETWEEN [between a range]
LIKE [pattern wildcard searches]
% [wildcard, multiple characters]
_ [wildcard, one character]
Below is a screenshot from the Osquery [documentation](https://osquery.readthedocs.io/en/stable/deployment/file-integrity-monitoring/) showing examples of using wildcards when used in folder structures.
![](https://assets.tryhackme.com/additional/osquery/osquery_wildcard.png)
Some tables will require a WHERE clause, such as the file table, to return a value. If the required WHERE clause is not included in the query, then you will get an error.
![](https://assets.tryhackme.com/additional/osquery/osquery_fileerror.png)
The last concept to cover is JOIN. To join 2 or more tables, each table needs to share a column in common.
Let's look at 2 tables to demonstrate this further. Below is the schema for the osquery_info table and the processes table.
The common column in both tables is pid. A query can be constructed to use the JOIN clause to join these 2 tables USING the PID column.
Query: `SELECT pid, name, path FROM osquery_info JOIN processes USING (pid);`
![](https://assets.tryhackme.com/additional/osquery/osquery_join.png)
```text
osquery> .schema osquery_info
CREATE TABLE osquery_info(`pid` INTEGER, `uuid` TEXT, `instance_id` TEXT, `version` TEXT, `config_hash` TEXT, `config_valid` INTEGER, `extensions` TEXT, `build_platform` TEXT, `build_distro` TEXT, `start_time` INTEGER, `watcher` INTEGER, `platform_mask` INTEGER);
osquery> .schema processes
CREATE TABLE processes(`pid` BIGINT, `name` TEXT, `path` TEXT, `cmdline` TEXT, `state` TEXT, `cwd` TEXT, `root` TEXT, `uid` BIGINT, `gid` BIGINT, `euid` BIGINT, `egid` BIGINT, `suid` BIGINT, `sgid` BIGINT, `on_disk` INTEGER, `wired_size` BIGINT, `resident_size` BIGINT, `total_size` BIGINT, `user_time` BIGINT, `system_time` BIGINT, `disk_bytes_read` BIGINT, `disk_bytes_written` BIGINT, `start_time` BIGINT, `parent` BIGINT, `pgroup` BIGINT, `threads` INTEGER, `nice` INTEGER, `is_elevated_token` INTEGER, `elapsed_time` BIGINT, `handle_count` BIGINT, `percent_processor_time` BIGINT, `upid` BIGINT HIDDEN, `uppid` BIGINT HIDDEN, `cpu_type` INTEGER HIDDEN, `cpu_subtype` INTEGER HIDDEN, `phys_footprint` BIGINT HIDDEN, PRIMARY KEY (`pid`)) WITHOUT ROWID;
osquery> select pid, name, path from osquery_info join processes using (pid);
+------+--------------+----------------------------------------------------+
| pid  | name         | path                                               |
+------+--------------+----------------------------------------------------+
| 5880 | osqueryi.exe | C:\ProgramData\chocolatey\lib\osquery\osqueryi.exe |
+------+--------------+----------------------------------------------------+
```
Please refer to the Osquery [documentation](https://osquery.readthedocs.io/en/stable/introduction/sql/) for more information regarding SQL and creating queries specific to Osquery.
