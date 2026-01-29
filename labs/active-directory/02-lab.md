
# Lab 02 – Active Directory & IT Fundamentals

## Objective
Set up a Windows Server domain, join a client VM, and manage users and groups.

## Environment
- Dell OptiPlex 3050 Micro, 16 GB RAM
- Proxmox VE
- Windows Server VM (Domain Controller)
- Windows 10/11 Client VM
- Domain: lab.local

## Tools & Software
- Active Directory Users & Computers
- Group Policy Management Console

## Steps Performed
1. Installed Windows Server VM
2. Configured static IP
3. Promoted server to Domain Controller
4. Created domain `lab.local`
5. Created OUs for Users and Computers
6. Added test user accounts
7. Joined Windows 10 client VM to domain
8. Verified logins and group policies

## Screenshots
- Save screenshots in `screenshots/active-directory/`
- Reference like:
```markdown
![AD Users](../../screenshots/active-directory/ad-users.png)
![Client Join](../../screenshots/active-directory/client-join.png)
