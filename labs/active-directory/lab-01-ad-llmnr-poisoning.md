Objective

The objective of this lab was to deploy a Windows Server 2022 Domain Controller, simulate a local network credential theft attack (LLMNR/NBT-NS poisoning), and document the remediation process using Group Policy Objects (GPOs).



Environment

Operating System (Target): Windows Server 2022 (Domain Controller)



Operating System (Attacker): Kali Linux



Security Tool: Responder (Python script)



Network: Isolated Proxmox Virtual Switch



Scenario

An attacker gained access to the internal network and utilized Responder to listen for legacy broadcast protocols. A domain user attempted to access a non-existent network share, broadcasting their NTLMv2 hash, which the attacker captured.



Incident Response Process

Phase 1 – Identification

The attacker machine (Kali Linux) was staged on the local network running Responder to listen for LLMNR and NBT-NS broadcasts.

The Windows Server user attempted to navigate to a typoed network share (e.g., \\\\filesrvver).



Phase 2 – Analysis

Because the DNS server could not resolve the typo, the Windows machine broadcasted an LLMNR request to the entire network.

Responder answered the broadcast, pretending to be the file server, and requested authentication.



Captured Data: Administrator NTLMv2 Hash



Vulnerable Protocols: LLMNR (UDP 5355) and NBT-NS (UDP 137)

(You will put a screenshot here of Kali Linux capturing the hash)



Phase 3 – Containment

To stop the immediate broadcast of credentials, a new Group Policy Object (GPO) was created in the Active Directory Domain to disable legacy name resolution protocols.



Action Taken: Navigated to Group Policy Management and created a policy named "Disable-LLMNR".

(You will put a screenshot here of the Group Policy Management Console)



Phase 4 – Eradication

The GPO was configured to permanently eradicate the vulnerability:



Path: Computer Configuration → Administrative Templates → Network → DNS Client



Setting: "Turn off multicast name resolution" set to Enabled.

Network adapter settings were also updated via DHCP to disable NetBIOS over TCP/IP.



Phase 5 – Recovery

Group policy was forced to update across the domain using the command gpupdate /force.

The simulated attack was run a second time. Responder captured zero hashes, confirming the network was secured against this attack vector.

(You will put a screenshot here of the failed second attack)



Findings

LLMNR and NBT-NS are legacy protocols enabled by default in Windows environments.



When DNS fails, Windows falls back to broadcasting credentials to the local network.



Group Policy is a highly effective, centralized tool for disabling vulnerable legacy protocols across an entire enterprise.



Security Impact

Exposed NTLMv2 hashes can be cracked offline using tools like Hashcat or used in NTLM Relay attacks, potentially leading to total domain compromise and privilege escalation.



Lessons Learned

Default configurations in enterprise software are often insecure for modern environments.



Disabling unnecessary broadcast protocols significantly reduces the internal attack surface.



Centralized configuration management (GPOs) is critical for maintaining a secure baseline.

