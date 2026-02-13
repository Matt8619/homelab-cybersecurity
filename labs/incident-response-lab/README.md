\# Lab 02 – Incident Response (Windows Defender Malware Detection)



\## Objective



The objective of this lab was to simulate a malware incident and document the incident response process using Microsoft Defender Antivirus.



---



\## Environment



\- Operating System: Windows 10 VM

\- Security Tool: Microsoft Defender Antivirus

\- Test File: EICAR Anti-Malware Test File

\- Network: Isolated Virtual Machine



---



\## Scenario



A suspicious file (eicar.com) was downloaded to the system. The file triggered an antivirus alert, simulating a malware infection attempt.



---



\# Incident Response Process



\## Phase 1 – Identification



The EICAR test file was downloaded to the system. Microsoft Defender immediately detected the file as malicious.



![Detection Alert](screenshots/screenshot-01-detection.png)



---



\## Phase 2 – Analysis



The threat details were reviewed in Protection History.



\- Threat Name: EICAR-Test-File

\- Severity: Low

\- Detection Time: (insert timestamp)

\- Action Taken: Quarantined / Removed



!\[Protection History](screenshots/defender-ir/screenshot-02-protection-history.png)



Event logs were examined using Event Viewer.



Location:

Applications and Services Logs → Microsoft → Windows → Windows Defender → Operational



Relevant Event IDs:

\- 1116 (Malware detected)

\- 1117 (Malware action taken)



!\[Event Viewer Log](screenshots/defender-ir/screenshot-03-eventviewer.png)



---



\## Phase 3 – Containment



The threat was automatically quarantined by Microsoft Defender. No manual containment actions were required.



---



\## Phase 4 – Eradication



The system verified that the malicious file was removed or quarantined successfully.



No additional remediation steps were necessary.



---



\## Phase 5 – Recovery



A full system scan was performed to ensure no additional threats were present.



!\[Full Scan Running](screenshots/defender-ir/screenshot-04-fullscan.png)



Scan results confirmed the system was clean.



!\[Scan Results](screenshots/defender-ir/screenshot-05-scan-results.png)



---



\## Findings



\- Real-time protection successfully detected the malicious file.

\- The file was quarantined automatically.

\- Event logs provided forensic evidence of detection and action.

\- The system remained secure without manual intervention.



---



\## Security Impact



The exposed file represented a potential malware threat. Automated antivirus protection prevented system compromise.



---



\## Lessons Learned



\- Real-time monitoring is critical for endpoint protection.

\- Logging mechanisms provide valuable forensic evidence.

\- Immediate containment reduces risk exposure.



