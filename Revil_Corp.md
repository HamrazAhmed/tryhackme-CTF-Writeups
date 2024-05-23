# Revil_Corp — Writeup

## Overview
### Revil_Corp — Writeup
### Revil_Corp — Writeup

## Exploitation
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ xfreerdp /u:administrator /p:'letmein123!' /v:10.10.101.235
[17:16:55:731] [111859:111868] [WARN][com.freerdp.crypto] - Certificate verification failure 'self signed certificate (18)' at stack position 0
[17:16:55:731] [111859:111868] [WARN][com.freerdp.crypto] - CN = THM-REDLINE
[17:16:55:735] [111859:111868] [ERROR][com.freerdp.crypto] - @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[17:16:55:736] [111859:111868] [ERROR][com.freerdp.crypto] - @           WARNING: CERTIFICATE NAME MISMATCH!           @
[17:16:55:736] [111859:111868] [ERROR][com.freerdp.crypto] - @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[17:16:55:736] [111859:111868] [ERROR][com.freerdp.crypto] - The hostname used for this connection (10.10.101.235:3389) 
[17:16:55:736] [111859:111868] [ERROR][com.freerdp.crypto] - does not match the name given in the certificate:
[17:16:55:736] [111859:111868] [ERROR][com.freerdp.crypto] - Common Name (CN):
[17:16:55:736] [111859:111868] [ERROR][com.freerdp.crypto] -    THM-REDLINE
[17:16:55:736] [111859:111868] [ERROR][com.freerdp.crypto] - A valid certificate for the wrong name should NOT be trusted!
Certificate details for 10.10.101.235:3389 (RDP-Server):
        Common Name: THM-REDLINE
        Subject:     CN = THM-REDLINE
        Issuer:      CN = THM-REDLINE
        Thumbprint:  ca:eb:a4:4a:9d:6b:94:59:25:57:c0:47:8d:24:84:1e:b5:bf:0d:3a:31:56:54:7c:8f:6e:e2:51:7f:1c:8d:dc
The above X.509 certificate could not be verified, possibly because you do not have
the CA certificate in your certificate store, or the certificate has expired.
Please look at the OpenSSL documentation on how to add a private CA to the store.
Do you trust the above certificate? (Y/T/N) Y
[17:17:03:826] [111859:111868] [ERROR][com.winpr.timezone] - Unable to find a match for unix timezone: US/Eastern
[17:17:03:436] [111859:111868] [INFO][com.freerdp.gdi] - Local framebuffer format  PIXEL_FORMAT_BGRX32
[17:17:03:436] [111859:111868] [INFO][com.freerdp.gdi] - Remote framebuffer format PIXEL_FORMAT_BGRA32
[17:17:04:909] [111859:111868] [INFO][com.freerdp.channels.rdpsnd.client] - [static] Loaded fake backend for rdpsnd
[17:17:04:910] [111859:111868] [INFO][com.freerdp.channels.drdynvc.client] - Loading Dynamic Virtual Channel rdpgfx
[17:17:05:590] [111859:111868] [WARN][com.freerdp.client.x11] - xf_lock_x11_:  [1] recursive lock from xf_process_x_events
[17:17:05:591] [111859:111868] [WARN][com.freerdp.client.x11] - xf_lock_x11_:  [1] recursive lock from xf_process_x_events
[17:17:05:782] [111859:111868] [WARN][com.freerdp.client.x11] - xf_lock_x11_:  [1] recursive lock from xf_process_x_events
[17:17:05:852] [111859:111868] [WARN][com.freerdp.client.x11] - xf_lock_x11_:  [1] recursive lock from xf_process_x_events

USING REDLINE
What is the compromised employee's full name? user -> John Coleman (because last login)

What is the operating system of the compromised host? System Information -> Windows 7 Home Premium 7601 Service Pack 1

What is the name of the malicious executable that the user opened?
WinRAR2021.exe

What is the full URL that the user visited to download the malicious binary? (include the binary as well)
file download history-> http://192.168.75.129:4748/Documents/WinRAR2021.exe

