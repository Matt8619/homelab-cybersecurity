\# Nmap Lab - Network Enumeration



\## Objective

Perform basic network enumeration using Nmap to discover open ports and services.



\## Lab Steps

1\. Launch Nmap against the target IP.

2\. Use common scan options:

&nbsp;  - `nmap -sS <target>` for SYN scan

&nbsp;  - `nmap -sV <target>` for service/version detection

3\. Document the open ports and services found.



\## Findings

| Port | Service | Version |

|------|---------|---------|

| 22   | SSH     | OpenSSH 8.9 |

| 80   | HTTP    | Apache 2.4.52 |



\## Summary

This lab demonstrates how to discover hosts, open ports, and running services in a network using Nmap.



