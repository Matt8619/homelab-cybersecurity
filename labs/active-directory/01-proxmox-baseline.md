# Lab 01 – Proxmox Baseline Setup

## Objective
Document the baseline infrastructure used for the home lab, including hardware,
virtualization platform, and initial virtual machines.

## Environment

### Hardware
- Dell OptiPlex 3050 Micro
- 16 GB RAM
- Gigabit Ethernet connection
- Raspberry Pi 4

### Virtualization Platform
- Proxmox VE
- Storage configuration: (local-lvm, local, etc.)

### Virtual Machines
| VM Name | OS | RAM | Purpose |
|------|----|----|--------|
| ubuntu-server | Ubuntu Server | 1 GB | General server / logging |
| windows-client | Windows 10/11 | 4 GB | User workstation |
| kali-linux | Kali Linux | 2 GB | Security testing |

## Network Configuration
- Bridged networking
- Private LAN (192.168.x.0/24)

## Steps Performed
1. Installed Proxmox VE on Dell OptiPlex hardware
2. Configured network bridge for VM connectivity
3. Created initial virtual machines
4. Verified VM-to-VM network communication

## Validation
- Confirmed all VMs boot successfully
- Verified network connectivity using ping
- Accessed Proxmox web interface for management

## What I Learned
This lab reinforced core virtualization concepts, VM lifecycle management,
and the importance of documenting infrastructure before adding services.
