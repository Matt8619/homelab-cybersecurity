\# Lab 01 – Nmap Network Enumeration



\## Objective

The goal of this lab was to perform network enumeration using Nmap in order to identify live hosts, open ports, and running services on a target system.



\## Environment

\- Attacker Machine: Kali Linux

\- Target Machine: Metasploitable2

\- Network Type: Host-only / Internal lab network



\## Tools Used

\- Nmap



\## Steps Performed



\### Step 1: Host Discovery

A ping sweep was performed to identify live hosts on the network.



!\[Host Discovery](../../screenshots/nmap/Screenshot-01-host-discovery.png)



\### Step 2: Port Scanning

A full TCP scan was run against the target to identify open ports.



!\[Port Scan](../../screenshots/nmap/Screenshot-02-port-scan.png)



\### Step 3: Service and Version Detection

Service version detection was used to identify running services and their versions.



!\[Service Detection](../../screenshots/nmap/Screenshot-03-service-detection.png)



\## Findings

\- Multiple open ports were discovered including FTP, SSH, HTTP, and MySQL.

\- Several services were outdated and known to contain vulnerabilities.

\- The results indicate the system is highly insecure and suitable for exploitation.



\## Security Impact

Exposed services increase the attack surface and can allow attackers to gain unauthorized access if vulnerabilities are exploited.



\## Mitigation Recommendations

\- Close unused ports

\- Update vulnerable services

\- Implement firewall rules to restrict access



