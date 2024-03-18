---
Let's cover the basics of Osquery.
---

# Osquery The Basics — Writeup

## Overview
### Osquery The Basics — Writeup
### Osquery The Basics — Writeup
### Introduction
[Osquery](https://osquery.io/) is an open-source agent created by [Facebook](https://engineering.fb.com/2014/10/29/security/introducing-osquery/) in 2014. It converts the operating system into a relational database. It allows us to ask questions from the tables using SQL queries, like returning the list of running processes, a user account created on the host, and the process of communicating with certain suspicious domains. It is widely used by Security Analysts, Incident Responders, Threat Hunters, etc. Osquery can be installed on multiple platforms: Windows, Linux, macOS, and FreeBSD.
Learning Objective
In this introductory room, the following learning objectives are covered:
What is Osquery, and what problem it solves?
Osquery in Interactive Mode
How to use the interactive mode of Osquery to interact with the operating system
How to join two tables to get a single answer
Note: It is highly beneficial if you're already familiar with SQL queries. If not, check out this [SQL Tutorial](https://www.w3schools.com/sql/sql_intro.asp).
### Connect with the Lab
The virtual machine attached to this room already has Osquery installed and configured for you on Windows and Linux. Before proceeding, start the attached VM and use the following credentials to connect. The VM will be accessible in the split screen on the right side. In case the VM is not visible, use the blue Show Split View button at the top-right of the page.
Click on the powershell terminal pinned at the taskbar and enter osqueryi to enter the interactive mode of osquery.
Machine IP: MACHINE_IP
Username: James
Password: thm_4n6
Note that it will take 3-5 minutes for the VM to boot up completely.
### Osquery: Interactive Mode
One of the ways to interact with Osquery is by using the interactive mode. Open the terminal and run run osqueryi. To understand the tool, run the .help command in the interactive terminal, as shown below:
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery> .help
Welcome to the osquery shell. Please explore your OS!
You are connected to a transient 'in-memory' virtual database.

.all [TABLE]     Select all from a table
.bail ON|OFF     Stop after hitting an error
.connect PATH    Connect to an osquery extension socket
.disconnect      Disconnect from a connected extension socket
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
.socket          Show the local osquery extensions socket path
.show            Show the current values for various settings
.summary         Alias for the show meta command
.tables [TABLE]  List names of tables
.types [SQL]     Show result of getQueryColumns for the given query
.width [NUM1]+   Set column widths for "column" mode
.timer ON|OFF      Turn the CPU timer measurement on or off
```
Note: As per the documentation, meta-commands are prefixed with a ..
List the tables
To list all the available tables that can be queried, use the .tables meta-command.
For example, if you wish to check what tables are associated with processes, you can use .tables process.
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery> .table 
=> appcompat_shims
  => arp_cache
  => atom_packages
  => authenticode
  => autoexec
  => azure_instance_metadata
  => azure_instance_tags
  => background_activities_moderator
  => bitlocker_info
  => carbon_black_info
  => carves
  => certificates
  => chassis_info
  => chocolatey_packages
```
To list all the tables with the term user in them, we will use .tables user as shown below:
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery> .table user
  => user_groups
  => user_ssh_keys
  => userassist
  => users
```
In the above example, four tables are returned that contain the word user.
Understanding the table Schema
Table names are not enough to know what information it contains without actually querying it. Knowledge of columns and types (known as a schema ) for each table is also helpful.
We can list a table's schema with the following meta-command: .schema table_name
Here, we are interested in understanding the columns in the user's table.
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery> .schema users
CREATE TABLE users(`uid` BIGINT, `gid` BIGINT, `uid_signed` BIGINT, `gid_signed` BIGINT, `username` TEXT, `description` TEXT, `directory` TEXT, `shell` TEXT, `uuid` TEXT, `type` TEXT, `is_hidden` INTEGER HIDDEN, `pid_with_namespace` INTEGER HIDDEN, PRIMARY KEY (`uid`, `username`, `uuid`, `pid_with_namespace`)) WITHOUT ROWID;
```
The above result provides the column names like username, description, PID followed by respective datatypes like BIGINT, TEXT, INTEGER, etc. Let us pick a few columns from this schema and use SQL query to ask osquery to display the columns from the user table using the following syntax:
SQL QUERY SYNTAX: select column1, column2, column3 from table;
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery>select gid, uid, description, username, directory from users;
+-----+------+------------------------------------------------------------+----------------------+-------------------------------------------+
| gid | uid  | description                                                | username           | directory                                   |
+-----+------+-------------------------------------------------------------------------------------------------------------------------------+
| 544 | 500  | Built-in account for administering the computer/domain     | Administrator      |                                             |
| 581 | 503  | A user account managed by the system.                      | DefaultAccount     |                                             |
| 546 | 501  | Built-in account for guest access to the computer/domain   | Guest              |                                             |
| 544 | 1002 |                                                            | James              | C:\Users\James                              |
| 18  | 18   |                                                            | SYSTEM             | %systemroot%\system32\config\systemprofile  |
| 19  | 19   |                                                            | LOCAL SERVICE      | %systemroot%\ServiceProfiles\LocalService   |
| 20  | 20   |                                                            | NETWORK SERVICE    | %systemroot%\ServiceProfiles\NetworkService |
+-----+------+------------------------------------------------------------+--------------------+----------------
```
Display Mode
Osquery comes with multiple display modes to select from. Use the .help option to list the available modes or choose 1 of them as shown below:
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery>.help
Welcome to the osquery shell. Please explore your OS!
You are connected to a transient 'in-memory' virtual database.
.
.
.
.mode MODE       Set output mode where MODE is one of:
                   csv      Comma-separated values
                   column   Left-aligned columns see .width
                   line     One value per line
                   list     Values delimited by .separator string
                   pretty   Pretty printed SQL results (default)
.
.
.
```
The schema API online documentation can be used to view a complete list of tables, columns, types, and column descriptions.
How many tables are returned when we query "table process" in the interactive mode of Osquery?
```text
osquery> .tables process
  => process_memory_map
  => process_open_sockets
  => processes
```
*3*
Looking at the schema of the processes table, which column displays the process id for the particular process?
```text
osquery> .schema processes
CREATE TABLE processes(`pid` BIGINT, `name` TEXT, `path` TEXT, `cmdline` TEXT, `state` TEXT, `cwd` TEXT, `root` TEXT, `uid` BIGINT, `gid` BIGINT, `euid` BIGINT, `egid` BIGINT, `suid` BIGINT, `sgid` BIGINT, `on_disk` INTEGER, `wired_size` BIGINT, `resident_size` BIGINT, `total_size` BIGINT, `user_time` BIGINT, `system_time` BIGINT, `disk_bytes_read` BIGINT, `disk_bytes_written` BIGINT, `start_time` BIGINT, `parent` BIGINT, `pgroup` BIGINT, `threads` INTEGER, `nice` INTEGER, `elevated_token` INTEGER, `secure_process` INTEGER, `protection_type` TEXT, `virtual_process` INTEGER, `elapsed_time` BIGINT, `handle_count` BIGINT, `percent_processor_time` BIGINT, `upid` BIGINT HIDDEN, `uppid` BIGINT HIDDEN, `cpu_type` INTEGER HIDDEN, `cpu_subtype` INTEGER HIDDEN, `translated` INTEGER HIDDEN, `cgroup_path` TEXT HIDDEN, `phys_footprint` BIGINT HIDDEN, PRIMARY KEY (`pid`)) WITHOUT ROWID;
osquery> select pid from processes;
+------+
| pid  |
+------+
| 0    |
| 4    |
| 88   |
| 424  |
| 596  |
| 672  |
| 724  |
| 744  |
| 812  |
| 832  |
| 940  |
| 960  |
| 988  |
| 992  |
| 516  |
| 548  |
| 540  |
| 1064 |
| 1080 |
| 1144 |
| 1164 |
| 1232 |
| 1256 |
| 1376 |
| 1412 |
| 1428 |
| 1500 |
| 1560 |
| 1596 |
| 1604 |
| 1616 |
| 1676 |
| 1700 |
| 1780 |
| 1788 |
| 1904 |
| 1956 |
| 2000 |
| 1520 |
| 2072 |
| 2188 |
| 2196 |
| 2204 |
| 2328 |
| 2400 |
| 2476 |
| 2568 |
| 2604 |
| 2664 |
| 2676 |
| 2708 |
| 2744 |
| 2752 |
| 2768 |
| 2776 |
| 2784 |
| 2864 |
| 2976 |
| 3012 |
| 2892 |
| 3084 |
| 3776 |
| 4004 |
| 3968 |
| 4244 |
| 4252 |
| 5108 |
| 4064 |
| 3804 |
| 1396 |
| 5100 |
| 2224 |
| 1888 |
| 2836 |
| 2908 |
| 4432 |
| 4152 |
| 4532 |
| 4612 |
| 4656 |
| 4776 |
| 3464 |
| 856  |
| 2960 |
| 1640 |
| 4468 |
| 4444 |
| 2576 |
| 3136 |
| 4848 |
| 1820 |
| 5288 |
| 5648 |
| 5788 |
| 5796 |
| 6056 |
| 5720 |
| 2324 |
| 5840 |
| 6664 |
| 3452 |
| 4720 |
| 5252 |
| 6596 |
| 1052 |
| 3276 |
| 2148 |
| 5444 |
| 7096 |
| 4992 |
| 4552 |
+------+
```
*pid*
Examine the .help command, how many output display modes are available for the .mode command?
```text
osquery> .help
Welcome to the osquery shell. Please explore your OS!
You are connected to a transient 'in-memory' virtual database.

.all [TABLE]     Select all from a table
.bail ON|OFF     Stop after hitting an error
.connect PATH    Connect to an osquery extension socket
.disconnect      Disconnect from a connected extension socket
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
.socket          Show the local osquery extensions socket path
.show            Show the current values for various settings
.summary         Alias for the show meta command
.tables [TABLE]  List names of tables
.types [SQL]     Show result of getQueryColumns for the given query
.width [NUM1]+   Set column widths for "column" mode
.timer ON|OFF      Turn the CPU timer measurement on or off
osquery> .mode pretty
```
*5*
```text
PS C:\Users\James> osqueryi
Using a [1mvirtual database[0m. Need help, type '.help'
osquery> .help
Welcome to the osquery shell. Please explore your OS!
You are connected to a transient 'in-memory' virtual database.

.all [TABLE]     Select all from a table
.bail ON|OFF     Stop after hitting an error
.connect PATH    Connect to an osquery extension socket
.disconnect      Disconnect from a connected extension socket
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
.socket          Show the local osquery extensions socket path
.show            Show the current values for various settings
.summary         Alias for the show meta command
.tables [TABLE]  List names of tables
.types [SQL]     Show result of getQueryColumns for the given query
.width [NUM1]+   Set column widths for "column" mode
.timer ON|OFF      Turn the CPU timer measurement on or off
osquery> .tables
  => appcompat_shims
  => arp_cache
  => atom_packages
  => authenticode
  => autoexec
  => azure_instance_metadata
  => azure_instance_tags
  => background_activities_moderator
  => bitlocker_info
  => carbon_black_info
  => carves
  => certificates
  => chassis_info
  => chocolatey_packages
  => chrome_extension_content_scripts
  => chrome_extensions
  => connectivity
  => cpu_info
  => cpuid
  => curl
  => curl_certificate
  => default_environment
  => device_file
  => device_hash
  => device_partitions
  => disk_info
  => dns_cache
  => drivers
  => ec2_instance_metadata
  => ec2_instance_tags
  => etc_hosts
  => etc_protocols
  => etc_services
  => file
  => firefox_addons
  => groups
  => hash
  => hvci_status
  => ie_extensions
  => intel_me_info
  => interface_addresses
  => interface_details
  => kernel_info
  => kva_speculative_info
  => listening_ports
  => logged_in_users
  => logical_drives
  => logon_sessions
  => memory_devices
  => npm_packages
  => ntdomains
  => ntfs_acl_permissions
  => ntfs_journal_events
  => office_mru
  => os_version
  => osquery_events
  => osquery_extensions
  => osquery_flags
  => osquery_info
  => osquery_packs
  => osquery_registry
  => osquery_schedule
  => patches
  => physical_disk_performance
  => pipes
  => platform_info
  => powershell_events
  => prefetch
  => process_memory_map
  => process_open_sockets
  => processes
  => programs
  => python_packages
  => registry
  => routes
  => scheduled_tasks
  => secureboot
  => services
  => shared_resources
  => shellbags
  => shimcache
  => ssh_configs
  => startup_items
  => system_info
  => time
  => tpm_info
  => uptime
  => user_groups
  => user_ssh_keys
  => userassist
  => users
  => video_info
  => winbaseobj
  => windows_crashes
  => windows_eventlog
  => windows_events
  => windows_firewall_rules
  => windows_optional_features
  => windows_security_center
  => windows_security_products
  => windows_update_history
  => wmi_bios_info
  => wmi_cli_event_consumers
  => wmi_event_filters
  => wmi_filter_consumer_binding
  => wmi_script_event_consumers
  => yara
  => ycloud_instance_metadata
osquery> .tables process
  => process_memory_map
  => process_open_sockets
  => processes
osquery> .tables user
  => user_groups
  => user_ssh_keys
  => userassist
  => users
osquery> .schema users
CREATE TABLE users(`uid` BIGINT, `gid` BIGINT, `uid_signed` BIGINT, `gid_signed` BIGINT, `username` TEXT, `description` TEXT, `directory` TEXT, `shell` TEXT, `uuid` TEXT, `type` TEXT, `is_hidden` INTEGER HIDDEN, `pid_with_namespace` INTEGER HIDDEN, PRIMARY KEY (`uid`, `username`, `uuid`, `pid_with_namespace`)) WITHOUT ROWID;
osquery> .schema user_ssh_keys
CREATE TABLE user_ssh_keys(`uid` BIGINT, `path` TEXT, `encrypted` INTEGER, `key_type` TEXT, `pid_with_namespace` INTEGER HIDDEN, PRIMARY KEY (`uid`, `path`, `pid_with_namespace`)) WITHOUT ROWID;
osquery> .schema yara
CREATE TABLE yara(`path` TEXT, `matches` TEXT, `count` INTEGER, `sig_group` TEXT, `sigfile` TEXT, `sigrule` TEXT HIDDEN, `strings` TEXT, `tags` TEXT, `sigurl` TEXT HIDDEN, PRIMARY KEY (`path`, `sig_group`, `sigfile`, `sigrule`, `sigurl`)) WITHOUT ROWID;
osquery> select gid, uid, description, username, directory from users;
+-----+------+-------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
| gid | uid  | description                                                                                     | username           | directory                                   |
+-----+------+-------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
| 544 | 1008 |                                                                                                 | 4n6lab             |                                             |
| 544 | 500  | Built-in account for administering the computer/domain                                          | Administrator      | C:\Users\Administrator                      |
| 544 | 1010 |                                                                                                 | art-test           |                                             |
| 581 | 503  | A user account managed by the system.                                                           | DefaultAccount     |                                             |
| 546 | 501  | Built-in account for guest access to the computer/domain                                        | Guest              |                                             |
| 544 | 1009 | Creative Artist                                                                                 | James              | C:\Users\James                              |
| 513 | 504  | A user account managed and used by the system for Windows Defender Application Guard scenarios. | WDAGUtilityAccount |                                             |
| 18  | 18   |                                                                                                 | SYSTEM             | %systemroot%\system32\config\systemprofile  |
| 19  | 19   |                                                                                                 | LOCAL SERVICE      | %systemroot%\ServiceProfiles\LocalService   |
| 20  | 20   |                                                                                                 | NETWORK SERVICE    | %systemroot%\ServiceProfiles\NetworkService |
+-----+------+-------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
```
### Schema Documentation
For this task, go to the schema [documentation](https://osquery.io/schema/5.5.1/) of Osquery version 5.5.1, the latest version. The schema documentation looks like the image shown below:
Breakdown
Let's break down the important information we could find in this schema documentation:
A dropdown lists various versions of Osquery. Choose the version of Osquery you wish to see schema tables for.
The number of tables within the selected version of Osquery. (In the above image, 106 tables are available).
The list of tables is listed in alphabetical order for the selected version of Osquery. This is the same result we get when we use the .table command in the interactive mode.
The name of the table and a brief description.
A detailed chart showing each table's column, type, and description.
Information to which Operating System the table applies. (In the above image, the account_policy_data table is available only for macOS)
A dropdown menu to select the Operating System of choice. We can choose multiple Operating Systems, which will display the tables available for those Operating systems.
You have enough information to navigate this resource to retrieve any necessary information confidently.
```text
106 tables in windows like documentation
osquery> .table
  => appcompat_shims
  => arp_cache
  => atom_packages
  => authenticode
  => autoexec
  => azure_instance_metadata
  => azure_instance_tags
  => background_activities_moderator
  => bitlocker_info
  => carbon_black_info
  => carves
  => certificates
  => chassis_info
  => chocolatey_packages
  => chrome_extension_content_scripts
  => chrome_extensions
  => connectivity
  => cpu_info
  => cpuid
  => curl
  => curl_certificate
  => default_environment
  => device_file
  => device_hash
  => device_partitions
  => disk_info
  => dns_cache
  => drivers
  => ec2_instance_metadata
  => ec2_instance_tags
  => etc_hosts
  => etc_protocols
  => etc_services
  => file
  => firefox_addons
  => groups
  => hash
  => hvci_status
  => ie_extensions
  => intel_me_info
  => interface_addresses
  => interface_details
  => kernel_info
  => kva_speculative_info
  => listening_ports
  => logged_in_users
  => logical_drives
  => logon_sessions
  => memory_devices
  => npm_packages
  => ntdomains
  => ntfs_acl_permissions
  => ntfs_journal_events
  => office_mru
  => os_version
  => osquery_events
  => osquery_extensions
  => osquery_flags
  => osquery_info
  => osquery_packs
  => osquery_registry
  => osquery_schedule
  => patches
  => physical_disk_performance
  => pipes
  => platform_info
  => powershell_events
  => prefetch
  => process_memory_map
  => process_open_sockets
  => processes
  => programs
  => python_packages
  => registry
  => routes
  => scheduled_tasks
  => secureboot
  => services
  => shared_resources
  => shellbags
  => shimcache
  => ssh_configs
  => startup_items
  => system_info
  => time
  => tpm_info
  => uptime
  => user_groups
  => user_ssh_keys
  => userassist
  => users
  => video_info
  => winbaseobj
  => windows_crashes
  => windows_eventlog
  => windows_events
  => windows_firewall_rules
  => windows_optional_features
  => windows_security_center
  => windows_security_products
  => windows_update_history
  => wmi_bios_info
  => wmi_cli_event_consumers
  => wmi_event_filters
  => wmi_filter_consumer_binding
  => wmi_script_event_consumers
  => yara
  => ycloud_instance_metadata
```
In Osquery version 5.5.1, how many common tables are returned, when we select both Linux and Window Operating system?
![[Pasted image 20221126181250.png]]
*56*
In Osquery version 5.5.1, how many tables for MAC OS are available?
![[Pasted image 20221126181317.png]]
*180*
In the Windows Operating system, which table is used to display the installed programs?
![[Pasted image 20221126181432.png]]
*programs*
In Windows Operating system, which column contains the registry value within the registry table?
![[Pasted image 20221126181549.png]]
*data*
### Creating SQL queries
The SQL language implemented in Osquery is not an entire SQL language that you might be accustomed to, but rather it's a superset of SQLite.
Realistically all your queries will start with a SELECT statement. This makes sense because, with Osquery, you are only querying information on an endpoint. You won't be updating or deleting any information/data on the endpoint.
The exception to the rule: Using other SQL statements, such as UPDATE and DELETE, is possible, but only if you're creating run-time tables (views) or using an extension if the extension supports them.
Your queries will also include a FROM clause and end with a semicolon.
Exploring Installed Programs
If you wish to retrieve all the information about the installed programs on the endpoint, first understand the table schema either using the .schema programs command in the interactive mode or use the documentation [here](https://osquery.io/schema/5.5.1/#programs).
Query: SELECT * FROM programs LIMIT 1;
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery>select * from programs limit 1;
              name = 7-Zip 21.07 (x64)
           version = 21.07
  install_location = C:\Program Files\7-Zip\
    install_source =
          language =
         publisher = Igor Pavlov
  uninstall_string = "C:\Program Files\7-Zip\Uninstall.exe"
      install_date =
identifying_number =
```
In the above example LIMIT was used followed by the number to limit the results to display.
Note: Your results will be different if you run this query in the attached VM or your local machine (if Osquery is installed). Here line mode is used to display the result.
The number of columns returned might be more than what you need. You can select specific columns rather than retrieve every column in the table.
Query: SELECT name, version, install_location, install_date from programs limit 1;
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery>select name, version, install_location, install_date from programs limit 1;
            name = 7-Zip 21.07 (x64)
         version = 21.07
install_location = C:\Program Files\7-Zip\
    install_date =
```
The above query will list the name, version, install location, and installed date of the programs on the endpoint. This will still return many results, depending on how busy the endpoint is.
Count
To see how many programs or entries in any table are returned, we can use the count() function, as shown below:
Query: SELECT count(*) from programs;
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery>select count(*) from programs;
count(*) = 160
```
WHERE Clause
Optionally, you can use a WHERE clause to narrow down the list of results returned based on specified criteria. The following query will first get the user table and only display the result for the user James, as shown below:
Query: SELECT * FROM users WHERE username='James';
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery>SELECT * FROM users WHERE username='James';
        uid = 1002
        gid = 544
 uid_signed = 1002
 gid_signed = 544
   username = James
description =
  directory = C:\Users\James
      shell = C:\Windows\system32\cmd.exe
       uuid = S-1-5-21-605937711-2036809076-574958819-1002
       type = local
```
The equal sign is not the only filtering option in a WHERE clause. Below are filtering operators that can be used in a WHERE clause:
= [equal]
<>  [not equal]
>, >= [greater than, greater than, or equal to]
<, <= [less than or less than or equal to]
BETWEEN [between a range]
LIKE [pattern wildcard searches]
% [wildcard, multiple characters]
_ [wildcard, one character]
Matching Wildcard Rules
Below is a screenshot from the Osquery [documentation](https://osquery.readthedocs.io/en/stable/deployment/file-integrity-monitoring/) showing examples of using wildcards when used in folder structures:
%: Match all files and folders for one level.
%%: Match all files and folders recursively.
%abc: Match all within-level ending in "abc".
abc%: Match all within-level starting with "abc".
Matching Examples
/Users/%/Library: Monitor for changes to every user's Library folder, but not the contents within.
/Users/%/Library/: Monitor for changes to files within each Library folder, but not the contents of their subdirectories.
/Users/%/Library/%: Same, changes to files within each Library folder.
/Users/%/Library/%%: Monitor changes recursively within each Library.
/bin/%sh: Monitor the bin directory for changes ending in sh.
Some tables require a WHERE clause, such as the file table, to return a value. If the required WHERE clause is not included in the query, then you will get an error.
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery>select * from file;
W1017 12:38:29.730041 45744 virtual_table.cpp:965] Table file was queried without a required column in the WHERE clause
W1017 12:38:29.730041 45744 virtual_table.cpp:976] Please see the table documentation: https://osquery.io/schema/#file
Error: constraint failed
```
Joining Tables using JOIN Function
OSquery can also be used to join two tables based on a column that is shared by both tables. Let's look at two tables to demonstrate this further. Below is the schema for the user's table and the processes table.
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery>.schema users
CREATE TABLE users(`uid` BIGINT, `gid` BIGINT, `uid_signed` BIGINT, `gid_signed` BIGINT, `username` TEXT, `description` TEXT, `directory` TEXT, `shell` TEXT, `uuid` TEXT, `type` TEXT, `is_hidden` INTEGER HIDDEN, `pid_with_namespace` INTEGER HIDDEN, PRIMARY KEY (`uid`, `username`, `uuid`, `pid_with_namespace`)) WITHOUT ROWID;

osquery>.schema processes
CREATE TABLE processes(`pid` BIGINT, `name` TEXT, `path` TEXT, `cmdline` TEXT, `state` TEXT, `cwd` TEXT, `root` TEXT, `uid` BIGINT, `gid` BIGINT, `euid` BIGINT, `egid` BIGINT, `suid` BIGINT, `sgid` BIGINT, `on_disk` INTEGER, `wired_size` BIGINT, `resident_size` BIGINT, `total_size` BIGINT, `user_time` BIGINT, `system_time` BIGINT, `disk_bytes_read` BIGINT, `disk_bytes_written` BIGINT, `start_time` BIGINT, `parent` BIGINT, `pgroup` BIGINT, `threads` INTEGER, `nice` INTEGER, `elevated_token` INTEGER, `secure_process` INTEGER, `protection_type` TEXT, `virtual_process` INTEGER, `elapsed_time` BIGINT, `handle_count` BIGINT, `percent_processor_time` BIGINT, `upid` BIGINT HIDDEN, `uppid` BIGINT HIDDEN, `cpu_type` INTEGER HIDDEN, `cpu_subtype` INTEGER HIDDEN, `translated` INTEGER HIDDEN, `cgroup_path` TEXT HIDDEN, `phys_footprint` BIGINT HIDDEN, PRIMARY KEY (`pid`)) WITHOUT ROWID;
```
Looking at both schemas, uid in users table is meant to identify the user record, and in the processes table, the column uid represents the user responsible for executing the particular process. We can join both tables using this uid field as shown below:
Query1: select uid, pid, name, path from processes;
Query2: select uid, username, description from users;
Joined Query: select p.pid, p.name, p.path, u.username from processes p JOIN users u on u.uid=p.uid LIMIT 10;
```text
--osquery interactive mode--

           
root@analyst$ osqueryi
Using a virtual database. Need help, type '.help'
osquery>select p.pid, p.name, p.path, u.username from processes p JOIN users u on u.uid=p.uid LIMIT 10;
+-------+-------------------+---------------------------------------+----------+
| pid   | name              | path                                  | username |
+-------+-------------------+---------------------------------------+----------+
| 7560  | sihost.exe        | C:\Windows\System32\sihost.exe        | James    |
| 6984  | svchost.exe       | C:\Windows\System32\svchost.exe       | James    |
| 7100  | svchost.exe       | C:\Windows\System32\svchost.exe       | James    |
| 7144  | svchost.exe       | C:\Windows\System32\svchost.exe       | James    |
| 8636  | ctfmon.exe        | C:\Windows\System32\ctfmon.exe        | James    |
| 8712  | taskhostw.exe     | C:\Windows\System32\taskhostw.exe     | James    |
| 9260  | svchost.exe       | C:\Windows\System32\svchost.exe       | James    |
| 10168 | RuntimeBroker.exe | C:\Windows\System32\RuntimeBroker.exe | James    |
| 10232 | RuntimeBroker.exe | C:\Windows\System32\RuntimeBroker.exe | James    |
| 8924  | svchost.exe       | C:\Windows\System32\svchost.exe       | James    |
+-------+-------------------+---------------------------------------+----------+
```
Note: Please refer to the Osquery [documentation](https://osquery.readthedocs.io/en/stable/introduction/sql/) for more information regarding SQL and creating queries specific to Osquery.

## Enumeration
```text
osquery> select * from programs;
+--------------------------------------------------------------------+---------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+----------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+----------------------------------------+
| name                                                               | version       | install_location                                         | install_source                                                                                                                     | language | publisher                                                    | uninstall_string                                                                                                                                          | install_date | identifying_number                     |
+--------------------------------------------------------------------+---------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+----------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+----------------------------------------+
| aws-cfn-bootstrap                                                  | 2.0.5         |                                                          | C:\ProgramData\Package Cache\{2C9F7E98-B055-4344-B8E4-58996F4A3B00}v2.0.5\                                                         | 1033     | Amazon Web Services                                          | MsiExec.exe /X{2C9F7E98-B055-4344-B8E4-58996F4A3B00}                                                                                                      | 20210311     | {2C9F7E98-B055-4344-B8E4-58996F4A3B00} |
| Microsoft Visual C++ 2022 X64 Minimum Runtime - 14.32.31332        | 14.32.31332   |                                                          | C:\ProgramData\Package Cache\{3407B900-37F5-4CC2-B612-5CD5D580A163}v14.32.31332\packages\vcRuntimeMinimum_amd64\                   | 1033     | Microsoft Corporation                                        | MsiExec.exe /I{3407B900-37F5-4CC2-B612-5CD5D580A163}                                                                                                      | 20221018     | {3407B900-37F5-4CC2-B612-5CD5D580A163} |
| AWS PV Drivers                                                     | 8.3.4         |                                                          | C:\ProgramData\Amazon\SSM\Packages\_arnawsssmpackageawspvdriver_21_66XA4XBKMUL56B6HYCFMNHV3CWSN44PIP4NHKIOMCDJMKGPGJE3A====\8.3.4\ | 1033     | Amazon Web Services                                          | MsiExec.exe /I{90C09D7C-18EB-4853-9F4F-D3040CC23924}                                                                                                      | 20200909     | {90C09D7C-18EB-4853-9F4F-D3040CC23924} |
| osquery                                                            | 5.5.1         | C:\Program Files\osquery\                                | C:\Users\James\Downloads\                                                                                                          | 1033     | osquery                                                      | MsiExec.exe /I{B55CDE5D-3EC9-4E57-AAD8-2B63BE889B46}                                                                                                      | 20221018     | {B55CDE5D-3EC9-4E57-AAD8-2B63BE889B46} |
| Amazon SSM Agent                                                   | 3.0.529.0     |                                                          | C:\ProgramData\Package Cache\{C1130551-76E8-44D6-A31D-4A9D5B0817CF}v3.0.529.0\                                                     | 1033     | Amazon Web Services                                          | MsiExec.exe /I{C1130551-76E8-44D6-A31D-4A9D5B0817CF}                                                                                                      | 20210311     | {C1130551-76E8-44D6-A31D-4A9D5B0817CF} |
| Microsoft Visual C++ 2022 X64 Additional Runtime - 14.32.31332     | 14.32.31332   |                                                          | C:\ProgramData\Package Cache\{F4499EE3-A166-496C-81BB-51D1BCDC70A9}v14.32.31332\packages\vcRuntimeAdditional_amd64\                | 1033     | Microsoft Corporation                                        | MsiExec.exe /I{F4499EE3-A166-496C-81BB-51D1BCDC70A9}                                                                                                      | 20221018     | {F4499EE3-A166-496C-81BB-51D1BCDC70A9} |
| Google Chrome                                                      | 107.0.5304.88 | C:\Program Files\Google\Chrome\Application               |                                                                                                                                    |          | Google LLC                                                   | "C:\Program Files\Google\Chrome\Application\107.0.5304.88\Installer\setup.exe" --uninstall --channel=stable --system-level --verbose-logging              | 20221104     |                                        |
| Microsoft Edge Update                                              | 1.3.169.31    |                                                          |                                                                                                                                    |          |                                                              |                                                                                                                                                           |              |                                        |
| Microsoft Edge WebView2 Runtime                                    | 107.0.1418.26 | C:\Program Files (x86)\Microsoft\EdgeWebView\Application |                                                                                                                                    |          | Microsoft Corporation                                        | "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\107.0.1418.26\Installer\setup.exe" --uninstall --msedgewebview --system-level --verbose-logging | 20221104     |                                        |
| Npcap                                                              | 1.60          | C:\Program Files\Npcap                                   |                                                                                                                                    |          | Nmap Project                                                 | "C:\Program Files\Npcap\uninstall.exe"                                                                                                                    |              |                                        |
| ProtonVPN                                                          | 2.0.6         | C:\Program Files (x86)\Proton Technologies\ProtonVPN\    |                                                                                                                                    |          | Proton Technologies AG                                       | msiexec.exe /i {E7AD46A7-6578-45D9-A690-BF58D33BA6B5} AI_UNINSTALLER_CTP=1                                                                                |              |                                        |
| Wireshark 3.6.8 64-bit                                             | 3.6.8         | C:\Program Files\Wireshark                               |                                                                                                                                    |          | The Wireshark developer community, https://www.wireshark.org | "C:\Program Files\Wireshark\uninstall.exe"                                                                                                                |              |                                        |
| Microsoft Visual C++ 2015-2022 Redistributable (x64) - 14.32.31332 | 14.32.31332.0 |                                                          |                                                                                                                                    |          | Microsoft Corporation                                        | "C:\ProgramData\Package Cache\{3746f21b-c990-4045-bb33-1cf98cff7a68}\VC_redist.x64.exe"  /uninstall                                                       |              | {3746f21b-c990-4045-bb33-1cf98cff7a68} |
| Amazon SSM Agent                                                   | 3.0.529.0     |                                                          |                                                                                                                                    |          | Amazon Web Services                                          | "C:\ProgramData\Package Cache\{674c5ef7-9d50-4540-a711-6b82e2469bd0}\AmazonSSMAgentSetup.exe"  /uninstall                                                 |              | {674c5ef7-9d50-4540-a711-6b82e2469bd0} |
| ProtonVPNTap                                                       | 1.1.4         | C:\Program Files (x86)\Proton Technologies\ProtonVPNTap\ | C:\Users\James\AppData\Local\Temp\{87BDF456-9882-44E6-8FFC-F73B83E42EAD}\3E42EAD\                                                  | 1033     | Proton Technologies AG                                       | MsiExec.exe /X{87BDF456-9882-44E6-8FFC-F73B83E42EAD}                                                                                                      | 20221018     | {87BDF456-9882-44E6-8FFC-F73B83E42EAD} |
| ProtonVPNTun                                                       | 0.13.1        | C:\Program Files (x86)\Proton Technologies\ProtonVPNTun\ | C:\Users\James\AppData\Local\Temp\{B1EBF050-CC3E-45B0-9DE5-339C6241F3DA}\241F3DA\                                                  | 1033     | Proton Technologies AG                                       | MsiExec.exe /X{B1EBF050-CC3E-45B0-9DE5-339C6241F3DA}                                                                                                      | 20221018     | {B1EBF050-CC3E-45B0-9DE5-339C6241F3DA} |
| aws-cfn-bootstrap                                                  | 2.0.5         |                                                          |                                                                                                                                    |          | Amazon Web Services                                          | "C:\ProgramData\Package Cache\{ba1812b9-5f2c-4e6a-b720-5cdd8247ad61}\aws-cfn-bootstrap-bundle.exe"  /uninstall                                            |              | {ba1812b9-5f2c-4e6a-b720-5cdd8247ad61} |
| AWS Tools for Windows                                              | 3.15.1248     |                                                          | C:\ec2amibuild\                                                                                                                    | 1033     | Amazon Web Services Developer Relations                      | MsiExec.exe /I{D08A7BB0-68D1-4A6A-B643-8A399E5CD84A}                                                                                                      | 20210311     | {D08A7BB0-68D1-4A6A-B643-8A399E5CD84A} |
| ProtonVPN                                                          | 2.0.6         | C:\Program Files (x86)\Proton Technologies\ProtonVPN\    | C:\Users\James\AppData\Local\Temp\{E7AD46A7-6578-45D9-A690-BF58D33BA6B5}\33BA6B5\                                                  | 1033     | Proton Technologies AG                                       | MsiExec.exe /I{E7AD46A7-6578-45D9-A690-BF58D33BA6B5}                                                                                                      | 20221018     | {E7AD46A7-6578-45D9-A690-BF58D33BA6B5} |
+--------------------------------------------------------------------+---------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+----------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+----------------------------------------+
osquery> select * from programs LIMIT 1;
+-------------------+---------+------------------+----------------------------------------------------------------------------+----------+---------------------+------------------------------------------------------+--------------+----------------------------------------+
| name              | version | install_location | install_source                                                             | language | publisher           | uninstall_string                                     | install_date | identifying_number                     |
+-------------------+---------+------------------+----------------------------------------------------------------------------+----------+---------------------+------------------------------------------------------+--------------+----------------------------------------+
| aws-cfn-bootstrap | 2.0.5   |                  | C:\ProgramData\Package Cache\{2C9F7E98-B055-4344-B8E4-58996F4A3B00}v2.0.5\ | 1033     | Amazon Web Services | MsiExec.exe /X{2C9F7E98-B055-4344-B8E4-58996F4A3B00} | 20210311     | {2C9F7E98-B055-4344-B8E4-58996F4A3B00} |
+-------------------+---------+------------------+----------------------------------------------------------------------------+----------+---------------------+------------------------------------------------------+--------------+----------------------------------------+
osquery> select * from programs LIMIT 1;
+-------------------+---------+------------------+----------------------------------------------------------------------------+----------+---------------------+------------------------------------------------------+--------------+----------------------------------------+
| name              | version | install_location | install_source                                                             | language | publisher           | uninstall_string                                     | install_date | identifying_number                     |
+-------------------+---------+------------------+----------------------------------------------------------------------------+----------+---------------------+------------------------------------------------------+--------------+----------------------------------------+
| aws-cfn-bootstrap | 2.0.5   |                  | C:\ProgramData\Package Cache\{2C9F7E98-B055-4344-B8E4-58996F4A3B00}v2.0.5\ | 1033     | Amazon Web Services | MsiExec.exe /X{2C9F7E98-B055-4344-B8E4-58996F4A3B00} | 20210311     | {2C9F7E98-B055-4344-B8E4-58996F4A3B00} |
+-------------------+---------+------------------+----------------------------------------------------------------------------+----------+---------------------+------------------------------------------------------+--------------+----------------------------------------+
osquery> select name, version, install_location, install_dat from programs limit 1;
Error: no such column: install_dat
osquery> select name, version, install_location, install_date from programs limit 1;
+-------------------+---------+------------------+--------------+
| name              | version | install_location | install_date |
+-------------------+---------+------------------+--------------+
| aws-cfn-bootstrap | 2.0.5   |                  | 20210311     |
+-------------------+---------+------------------+--------------+
osquery> select count(*) from programs;
+----------+
| count(*) |
+----------+
| 19       |
+----------+
osquery> select * from users;
+------+-----+------------+------------+--------------------+-------------------------------------------------------------------------------------------------+---------------------------------------------+-----------------------------+----------------------------------------------+---------+
| uid  | gid | uid_signed | gid_signed | username           | description                                                                                     | directory                                   | shell                       | uuid                                         | type    |
+------+-----+------------+------------+--------------------+-------------------------------------------------------------------------------------------------+---------------------------------------------+-----------------------------+----------------------------------------------+---------+
| 1008 | 544 | 1008       | 544        | 4n6lab             |                                                                                                 |                                             | C:\Windows\system32\cmd.exe | S-1-5-21-1966530601-3185510712-10604624-1008 | local   |
| 500  | 544 | 500        | 544        | Administrator      | Built-in account for administering the computer/domain                                          | C:\Users\Administrator                      | C:\Windows\system32\cmd.exe | S-1-5-21-1966530601-3185510712-10604624-500  | local   |
| 1010 | 544 | 1010       | 544        | art-test           |                                                                                                 |                                             | C:\Windows\system32\cmd.exe | S-1-5-21-1966530601-3185510712-10604624-1010 | local   |
| 503  | 581 | 503        | 581        | DefaultAccount     | A user account managed by the system.                                                           |                                             | C:\Windows\system32\cmd.exe | S-1-5-21-1966530601-3185510712-10604624-503  | local   |
| 501  | 546 | 501        | 546        | Guest              | Built-in account for guest access to the computer/domain                                        |                                             | C:\Windows\system32\cmd.exe | S-1-5-21-1966530601-3185510712-10604624-501  | local   |
| 1009 | 544 | 1009       | 544        | James              | Creative Artist                                                                                 | C:\Users\James                              | C:\Windows\system32\cmd.exe | S-1-5-21-1966530601-3185510712-10604624-1009 | local   |
| 504  | 513 | 504        | 513        | WDAGUtilityAccount | A user account managed and used by the system for Windows Defender Application Guard scenarios. |                                             | C:\Windows\system32\cmd.exe | S-1-5-21-1966530601-3185510712-10604624-504  | local   |
| 18   | 18  | 18         | 18         | SYSTEM             |                                                                                                 | %systemroot%\system32\config\systemprofile  | C:\Windows\system32\cmd.exe | S-1-5-18                                     | special |
| 19   | 19  | 19         | 19         | LOCAL SERVICE      |                                                                                                 | %systemroot%\ServiceProfiles\LocalService   | C:\Windows\system32\cmd.exe | S-1-5-19                                     | special |
| 20   | 20  | 20         | 20         | NETWORK SERVICE    |                                                                                                 | %systemroot%\ServiceProfiles\NetworkService | C:\Windows\system32\cmd.exe | S-1-5-20                                     | special |
+------+-----+------------+------------+--------------------+-------------------------------------------------------------------------------------------------+---------------------------------------------+-----------------------------+----------------------------------------------+---------+
osquery> select * from users where username='James';
+------+-----+------------+------------+----------+-----------------+----------------+-----------------------------+----------------------------------------------+-------+
| uid  | gid | uid_signed | gid_signed | username | description     | directory      | shell                       | uuid                                         | type  |
+------+-----+------------+------------+----------+-----------------+----------------+-----------------------------+----------------------------------------------+-------+
| 1009 | 544 | 1009       | 544        | James    | Creative Artist | C:\Users\James | C:\Windows\system32\cmd.exe | S-1-5-21-1966530601-3185510712-10604624-1009 | local |
+------+-----+------------+------------+----------+-----------------+----------------+-----------------------------+----------------------------------------------+-------+
osquery> .tables processes
  => processes
osquery> .schema processes
CREATE TABLE processes(`pid` BIGINT, `name` TEXT, `path` TEXT, `cmdline` TEXT, `state` TEXT, `cwd` TEXT, `root` TEXT, `uid` BIGINT, `gid` BIGINT, `euid` BIGINT, `egid` BIGINT, `suid` BIGINT, `sgid` BIGINT, `on_disk` INTEGER, `wired_size` BIGINT, `resident_size` BIGINT, `total_size` BIGINT, `user_time` BIGINT, `system_time` BIGINT, `disk_bytes_read` BIGINT, `disk_bytes_written` BIGINT, `start_time` BIGINT, `parent` BIGINT, `pgroup` BIGINT, `threads` INTEGER, `nice` INTEGER, `elevated_token` INTEGER, `secure_process` INTEGER, `protection_type` TEXT, `virtual_process` INTEGER, `elapsed_time` BIGINT, `handle_count` BIGINT, `percent_processor_time` BIGINT, `upid` BIGINT HIDDEN, `uppid` BIGINT HIDDEN, `cpu_type` INTEGER HIDDEN, `cpu_subtype` INTEGER HIDDEN, `translated` INTEGER HIDDEN, `cgroup_path` TEXT HIDDEN, `phys_footprint` BIGINT HIDDEN, PRIMARY KEY (`pid`)) WITHOUT ROWID;
osquery> .schema users
CREATE TABLE users(`uid` BIGINT, `gid` BIGINT, `uid_signed` BIGINT, `gid_signed` BIGINT, `username` TEXT, `description` TEXT, `directory` TEXT, `shell` TEXT, `uuid` TEXT, `type` TEXT, `is_hidden` INTEGER HIDDEN, `pid_with_namespace` INTEGER HIDDEN, PRIMARY KEY (`uid`, `username`, `uuid`, `pid_with_namespace`)) WITHOUT ROWID;
osquery> select p.pid, p.name, p.path, u.username from processes p join users u on u.uid=p.uid limit 10;
+------+-------------------------+---------------------------------------------------------------------------------+----------+
| pid  | name                    | path                                                                            | username |
+------+-------------------------+---------------------------------------------------------------------------------+----------+
| 1640 | rdpclip.exe             | C:\Windows\System32\rdpclip.exe                                                 | James    |
| 4468 | svchost.exe             | C:\Windows\System32\svchost.exe                                                 | James    |
| 4444 | svchost.exe             | C:\Windows\System32\svchost.exe                                                 | James    |
| 2576 | taskhostw.exe           | C:\Windows\System32\taskhostw.exe                                               | James    |
| 3136 | sihost.exe              | C:\Windows\System32\sihost.exe                                                  | James    |
| 1820 | ctfmon.exe              | C:\Windows\System32\ctfmon.exe                                                  | James    |
| 5288 | explorer.exe            | C:\Windows\explorer.exe                                                         | James    |
| 5648 | ShellExperienceHost.exe | C:\Windows\SystemApps\ShellExperienceHost_cw5n1h2txyewy\ShellExperienceHost.exe | James    |
| 5788 | SearchUI.exe            | C:\Windows\SystemApps\Microsoft.Windows.Cortana_cw5n1h2txyewy\SearchUI.exe      | James    |
| 5796 | RuntimeBroker.exe       | C:\Windows\System32\RuntimeBroker.exe                                           | James    |
+------+-------------------------+---------------------------------------------------------------------------------+----------+

doing exercises

osquery> select count(*) from programs;
+----------+
| count(*) |
+----------+
| 19       |
+----------+

osquery> select description from users where username='James';
+-----------------+
| description     |
+-----------------+
| Creative Artist |
+-----------------+

osquery> .schema registry
CREATE TABLE registry(`key` TEXT COLLATE NOCASE, `path` TEXT, `name` TEXT, `type` TEXT, `data` TEXT, `mtime` BIGINT, PRIMARY KEY (`key`, `path`)) WITHOUT ROWID;
osquery> select path, key, name from registry where key='HKEY_USERS';
+-----------------------------------------------------------------+------------+------------------------------------------------------+
| path                                                            | key        | name                                                 |
+-----------------------------------------------------------------+------------+------------------------------------------------------+
| HKEY_USERS\.DEFAULT                                             | HKEY_USERS | .DEFAULT                                             |
| HKEY_USERS\S-1-5-19                                             | HKEY_USERS | S-1-5-19                                             |
| HKEY_USERS\S-1-5-20                                             | HKEY_USERS | S-1-5-20                                             |
| HKEY_USERS\S-1-5-21-1966530601-3185510712-10604624-1009         | HKEY_USERS | S-1-5-21-1966530601-3185510712-10604624-1009         |
| HKEY_USERS\S-1-5-21-1966530601-3185510712-10604624-1009_Classes | HKEY_USERS | S-1-5-21-1966530601-3185510712-10604624-1009_Classes |
| HKEY_USERS\S-1-5-18                                             | HKEY_USERS | S-1-5-18                                             |
+-----------------------------------------------------------------+------------+------------------------------------------------------+

osquery> .schema ie_extensions
CREATE TABLE ie_extensions(`name` TEXT, `registry_path` TEXT, `version` TEXT, `path` TEXT);
osquery> select * from ie_extensions;
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------+
| name                      | registry_path                                                                                                                                      | version         | path                            |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------+
| Microsoft Url Search Hook | HKEY_USERS\S-1-5-21-1966530601-3185510712-10604624-1009\SOFTWARE\Microsoft\Internet Explorer\URLSearchHooks\{CFBFAE00-17A6-11D0-99CB-00C04FD64497} | 11.0.17763.3532 | C:\Windows\System32\ieframe.dll |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------+

osquery> .schema programs
CREATE TABLE programs(`name` TEXT, `version` TEXT, `install_location` TEXT, `install_source` TEXT, `language` TEXT, `publisher` TEXT, `uninstall_string` TEXT, `install_date` TEXT, `identifying_number` TEXT);
