### Automated SOC Security Pipeline: Technical Architecture & Implementation

This project details the development of an automated, virtualized Security Operations Center (SOC) lab environment designed for high-fidelity telemetry ingestion and threat visibility. The framework replaces traditional GUI dependency with a custom Python-based automation engine to bridge the gap between raw SIEM data and actionable intelligence.

#### Lab Infrastructure & Architecture

The lab environment is architected for scalability and security monitoring through the following stack:

* **Hypervisor**: Proxmox VE hosting an Ubuntu 22.04 Wazuh Manager.
* **Endpoints**: Windows 11 Enterprise (matt12) and Debian Bookworm.
* **Security Stack**: Wazuh v4.14 (All-in-One deployment).
* **Automation Interface**: Custom `ai_soc_analyst.py` wrapper, utilizing `requests` for JWT-authenticated API interactions.

#### Key Engineering Achievements

* **Infrastructure Resilience**: Addressed critical process-pool failures in the Wazuh API daemon by performing manual reconstruction of the `rbac.db` SQLite database and re-synchronizing credentials.
* **Custom Security Middleware**: Engineered a middleware tool capable of automated API authentication, token lifecycle management, and dynamic telemetry parsing to monitor critical security daemons in real-time.
* **Threat Hunting Pipeline**: Implemented a telemetry pipeline that bypasses static dashboard constraints, enabling programmatic querying of system-inventory and vulnerability data directly from endpoint agents.

#### Incident Lifecycle Simulation

The environment facilitates full-spectrum incident response testing:

* **Red Team**: Simulates lateral movement, brute-force attacks, and File Integrity Monitoring (FIM) modifications.
* **Blue Team**: Utilizes Wazuh’s native policy-monitoring and FIM modules for detection.
* **Triage**: Employs the `ai_soc_analyst` tool to automate alert parsing, significantly reducing the latency between initial log trigger and incident visibility.

#### Repository Organization

The environment is structured to support rapid restoration and modular development:

* `/scripts/ai_soc_analyst.py`: Core automation engine for threat detection and API communication.
* `/docs/troubleshooting_log.md`: Detailed documentation of infrastructure challenges and technical resolutions.
* `/config/`: Modular deployment configurations for rapid environment recovery.
