# Enterprise Active Directory Deployment, Administrative Tiering, & Account Hardening

## Project Objective
This project details the deployment of a virtualized corporate Active Directory environment using Windows Server 2022, the architecture of a secure administrative identity tiering system, and the implementation of enterprise-grade account security controls via Group Policy Objects (GPOs).

---

## 1. Infrastructure Architecture
To simulate a corporate corporate environment realistically, a dedicated virtual lab network was engineered with strict resource and network isolation.

### Host Hardware
* **System:** Dell OptiPlex 3050 Micro
* **Compute:** 16 GB RAM
* **Networking:** Gigabit Ethernet

### Hypervisor Layer & Topology
The environment is segmented using an isolated virtual switch within **Proxmox VE**, cutting off external internet traffic while permitting localized machine-to-machine routing.

| Hostname | Role / Operating System | IP Address Allocation | Purpose |
| :--- | :--- | :--- | :--- |
| **DC-SERVER-01** | Windows Server 2022 (Domain Controller) | 192.168.10.10 (Static) | Identity Governance & Domain DNS |
| **WIN-CLIENT-01** | Windows 10/11 Pro/Enterprise | 192.168.10.20 (DHCP) | Corporate User Workstation |

---

## 2. Active Directory Domain Services Initialization & Tiering
Before enforcing security baselines, the core identity infrastructure was provisioned from scratch.

1. **Active Directory Domain Services (AD DS):** Promoted `DC-SERVER-01` to a primary Domain Controller, establishing the internal forest root domain: `lab.local`.
2. **Organizational Unit (OU) Architecture:** Designed a clear administrative boundary by creating a dedicated `Corp-Users` OU. This prevents general users from mixing with infrastructure configurations.
3. **Identity Tiering Implementation:** To align with least-privilege security principles, two distinct accounts were created within the OU:
   * `mhyson-admin` (High-privilege account mapped explicitly to the **Domain Admins** group).
   * `jdoe-worker` (Standard, non-privileged employee account for general workstation tasks).

![Active Directory OU Structure](../../screenshots/active-directory/ad_ou_structure.png)

4. **Workstation Domain Join:** Configured network interface parameters on `WIN-CLIENT-01` to route primary DNS inquiries through the Domain Controller, completing a secure domain enrollment using administrative authentication.

---

## 3. Centralized Hardening via Group Policy Objects
To protect corporate identities against credential stuffing and brute-force guessing patterns, default Windows account vulnerabilities were remediated centrally using the **Group Policy Management Console (GPMC)**.

### Account Policy Configurations
A new GPO titled **"SecOps-Account-Hardening"** was generated and linked to the root domain container, enforcing three mandatory technical controls:

* **Minimum Password Length:** Enforced a strict minimum of **14 characters** to resist computational offline cracking speeds.
* **Complexity Requirements:** Enabled advanced filtering (requiring uppercase letters, lowercase letters, numbers, and symbols).
* **Account Lockout Threshold:** Restriced consecutive invalid logon attempts to a maximum of **5 failures** to block automated brute-force attacks.

![Group Policy Password Controls](../../screenshots/active-directory/gpo_password_policy.png)

### Enforcing Endpoint Compliance
To bypass default background replication delay cycles on the corporate workstation, policies were manually pushed over the terminal stack:
```powershell
gpupdate /force
