# AWS Cloud Operations & Automation Platform

## Project Overview

A hands-on AWS Cloud Engineering project focused on building, operating, monitoring, and automating cloud infrastructure.

The goal is to develop practical skills in AWS networking, Linux administration, cloud security, scripting, and incident response.

## Architecture

- AWS Region: us-east-1
- VPC: 10.0.0.0/16
- Public Subnet: 10.0.1.0/24
- Private Subnet: 10.0.2.0/24
- Internet Gateway and route tables
- EC2 Ubuntu 24.04 LTS web server
- IAM role for Systems Manager
- Security Groups controlling network access
- Nginx web server hosting a custom HTML page

## Implemented Features

### 1. AWS Infrastructure
- Created a custom VPC and public/private subnets
- Configured public internet routing
- Configured Security Groups
- Launched Ubuntu EC2 in the public subnet
- Established remote access using AWS Session Manager

### 2. Web Server Deployment
- Installed and configured Nginx
- Deployed a custom HTML webpage
- Verified local and browser-based HTTP access

### 3. Bash Automation
- Created a Nginx service health-check script
- Implemented automatic service recovery
- Scheduled recovery checks every minute using cron
- Tested failure detection and successful recovery

### 4. Python Monitoring
- Created a Python HTTP health-check script
- Tested successful and failed HTTP connections
- Implemented exit codes for automation integration
- Recorded basic health-check logs

## Repository Structure

    scripts/
    ├── bash/
    │   ├── nginx-health.sh
    │   └── nginx-recovery.sh
    └── python/
        └── website-health.py

## Technologies Used

AWS VPC | EC2 | IAM | Systems Manager | Ubuntu Linux |
Nginx | Bash | Python | Cron | Git | GitHub

## Project Roadmap

- [x] AWS networking and basic EC2 deployment
- [x] Nginx website deployment
- [x] Bash health checks and scheduled service recovery
- [x] Python HTTP health checks and exit codes
- [x] Initial GitHub repository and automation scripts
- [ ] Private application server and network security testing
- [ ] CloudWatch monitoring, logs, and alarms
- [ ] Python monitoring improvements
- [ ] CI/CD and Infrastructure as Code
- [ ] Production-style validation and documentation

## Current Status

Active development — infrastructure and core service automation implemented. Monitoring integration and advanced architecture are in progress.
