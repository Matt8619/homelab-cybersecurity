\# SOC Lab - Security Operations Basics



\## Objective

Demonstrate basic SOC analyst skills by identifying and documenting security events.



\## Scenario

A small organization is monitoring system and network activity.

Multiple alerts and logs were reviewed to identify suspicious behavior.



\## Data Reviewed

\- Windows security event logs

\- Network traffic alerts

\- Antivirus detection logs



\## Findings



| Event ID | Description                  | Severity | Analyst Notes |

|--------|------------------------------|----------|---------------|

| 4625   | Failed login attempt         | Medium   | Possible brute-force attempt |

| 4688   | Suspicious process creation | High     | Unknown executable launched |

| AV-101 | Malware detected             | High     | Host isolated |



\## Response Actions

\- Reviewed affected user accounts

\- Recommended password reset

\- Isolated infected host from network

\- Escalated incident to senior analyst



\## Conclusion

This lab demonstrates core SOC responsibilities including log review, alert triage,

severity classification, and response recommendations.



