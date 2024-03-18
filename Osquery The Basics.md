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
