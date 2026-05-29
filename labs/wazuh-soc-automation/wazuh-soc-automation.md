Project: Automated SOC Security Pipeline (Wazuh SIEM)
Overview
This project is an automated, virtualized Security Operations Center (SOC) lab environment. The goal was to build a self-healing security monitoring stack that could ingest telemetry from heterogeneous endpoints (Windows/Linux) and provide automated threat visibility via a custom-built API interface.

Instead of relying solely on the built-in GUI, I engineered a Python-based automation framework to bridge the gap between raw SIEM data and actionable security intelligence.

Architecture
Virtualization: Proxmox (Host) running Ubuntu 22.04 (Wazuh Manager).

Endpoints: Windows 11 Enterprise (matt12) and Debian Bookworm.

Security Stack: Wazuh v4.14 (All-in-One Deployment).

Automation: Custom Python ai_soc_analyst.py wrapper utilizing requests for JWT-authenticated API interaction.

Key Engineering Wins
Infrastructure Resilience: Resolved complex process-pool failures within the Wazuh API daemon, requiring manual reconstruction of the SQLite-based rbac.db and credential synchronization.

Security Automation: Developed a custom middleware tool that authenticates against the SIEM API, handles token management, and dynamically parses telemetry to provide real-time status of critical security daemons.

Threat Hunting Framework: Implemented a system-telemetry pipeline that bypasses static dashboard limitations, allowing for programmatic querying of vulnerability and system-inventory data directly from the endpoint agents.

Lab Highlights & Simulation
This environment is used to simulate the full lifecycle of an incident:

Red Team: Execution of lateral movement, brute-force simulations, and file-integrity modifications on Windows/Linux nodes.

Blue Team: Detection via Wazuh's FIM and policy-monitoring modules.

Triage: Automation of alert parsing using a Python-based analyst tool, reducing the time from "log trigger" to "incident visibility."

Repository Structure
/scripts/ai_soc_analyst.py: The core automation engine for API communication and threat detection.

/docs/troubleshooting_log.md: A technical breakdown of the infrastructure challenges and resolutions.

/config/: Simplified deployment configurations for rapid environment restoration.

Developed as part of my MS in Cybersecurity at Wilmington University. Focused on bridging the gap between infrastructure management and intelligent threat detection.
=======
# Cybersecurity \& IT Home Lab

## Overview

This repository documents a self-hosted cybersecurity and IT home lab built using Proxmox.
The lab is designed to demonstrate hands-on experience with virtualization, networking,
system administration, and security monitoring.

## Lab Environment

* Proxmox VE on Dell OptiPlex 3050 Micro
* Ubuntu Server, Kali Linux, Windows Server, Windows 10/11
* Raspberry Pi 4 for auxiliary services
* Gigabit Ethernet networking

## Skills Demonstrated

* Virtualization and VM management
* Active Directory administration
* Networking (DNS, DHCP, TCP/IP)
* Vulnerability scanning and risk analysis
* Log collection and monitoring (SIEM)
* Incident detection and response
* Backup and recovery
* Technical documentation

## Labs

\# Homelab Cybersecurity Portfolio



Hands-on cybersecurity labs demonstrating skills in network enumeration, web exploitation, and defensive analysis.



\## Labs



\- \[DVWA Web Exploitation](labs/dvwa/lab-01-dvwa-web-exploitation.md)

\- \[Nmap Network Enumeration](labs/nmap/lab-01-nmap-enumeration.md)

\- \[SOC Log Analysis](labs/soc/lab-01-soc-log-analysis.md)



* Proxmox Baseline Setup
* Active Directory Administration
* Network Services (DNS/DHCP)
* Centralized Logging and SIEM
* Vulnerability Scanning
* Incident Response Simulation

## Ethical Notice

All activities were performed in a controlled lab environment on systems I own.
No unauthorized scanning or exploitation was conducted.

>>>>>>> bba716e9cef1aec326b2517d9e8f197f9952dbf7
