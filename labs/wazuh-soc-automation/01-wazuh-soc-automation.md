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

