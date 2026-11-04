
# AWS Cloud Operations & Automation Platform

## Project Overview

A hands-on AWS Cloud Engineering project focused on designing, deploying, securing, monitoring, and troubleshooting a two-tier cloud application.

The project demonstrates AWS networking, Linux administration, Python and Bash automation, service recovery, monitoring, and incident troubleshooting.

## Architecture

**Region:** AWS us-east-1 (N. Virginia)

```text
             Client / Internet
                    |
             Internet Gateway
                    |
          Public Subnet 10.0.1.0/24
                    |
              Web EC2 (Nginx)
             Static Website /
                    |
          Reverse Proxy /app/
                    |
            Private TCP 8080
                    |
         Private Subnet 10.0.2.0/24
                    |
             App EC2 (Python)
               systemd service

     Amazon CloudWatch: EC2 CPU Monitoring
```

The private application server has no public IPv4 address. Network access is restricted through Security Groups.

See [Architecture Documentation](docs/architecture.md) for details.

## Implemented Features

### 1. AWS Networking and Security

- Created a custom VPC (`10.0.0.0/16`).
- Configured public and private subnets.
- Configured Internet Gateway and route tables.
- Implemented Security Group rules between application tiers.
- Tested public and private EC2 communication.
- Configured and tested a NAT Gateway for private outbound Internet access.
- Configured SSM Interface VPC Endpoints for private AWS management access.
- Used IAM roles and Session Manager for EC2 administration.

### 2. Web Server and Reverse Proxy

- Deployed an Ubuntu EC2 instance with Nginx.
- Hosted a custom static HTML website.
- Configured Nginx to forward `/app/` requests to the private Python application.
- Verified communication between public and private EC2 instances.
- Confirmed external browser access through Nginx.

### 3. Linux and Bash Automation

- Developed Nginx health-check and recovery scripts.
- Scheduled automated recovery checks using cron.
- Tested Nginx failure detection and recovery.
- Configured a Python application as a systemd service.
- Enabled automatic application startup during EC2 boot.
- Verified automatic recovery after terminating the Python process.

### 4. Python Application and Monitoring

- Deployed a Python HTTP server on private EC2 port 8080.
- Developed a Python HTTP health-check script with exit codes.
- Tested successful and failed HTTP connections.
- Implemented basic health-check logging.

### 5. Amazon CloudWatch

- Explored EC2 CPU utilization metrics.
- Created a CPU utilization alarm using a 10% threshold.
- Configured a five-minute evaluation period.
- Generated controlled CPU activity.
- Verified alarm transition from OK to ALARM.
- Verified automatic return to OK after CPU usage decreased.

The 10% threshold was chosen for testing, not as a production recommendation. No email notification action was configured.

## Troubleshooting and Validation

| Scenario | Observed Result |
|---|---|
| Private application responds locally | HTTP 200 |
| Web EC2 connects to private application | Successful |
| Nginx reverse proxy forwards `/app/` | HTTP 200 |
| Private Python application stopped | HTTP 502 from Nginx |
| Python application restored | HTTP 200 without Nginx restart |
| Python process forcibly terminated | systemd restarted process |
| EC2 operating system rebooted | Python service started automatically |
| Private EC2 accessed without NAT | Session Manager worked via VPC Endpoints |
| Controlled CPU usage exceeded threshold | CloudWatch entered ALARM |
| CPU usage returned to normal | CloudWatch returned to OK |

## Repository Structure

```text
aws-cloud-operations/
├── app/
│   └── server.py
├── config/
│   ├── aws-operations-app.service
│   └── nginx-reverse-proxy.conf
├── docs/
│   └── architecture.md
├── scripts/
│   ├── bash/
│   │   ├── nginx-health.sh
│   │   └── nginx-recovery.sh
│   └── python/
│       └── website-health.py
├── .gitignore
└── README.md
```

The repository includes a functionally equivalent reconstruction of the Python application and the configuration used in the exercises. The Nginx file is a configuration snippet intended to be inserted into an existing server block.

## Technologies Used

**AWS:** VPC, EC2, IAM, Systems Manager, CloudWatch, NAT Gateway, Interface VPC Endpoints, Security Groups

**Operating System:** Ubuntu Linux 24.04 LTS

**Web and Application:** Nginx, Python HTTP Server

**Automation:** Bash, Python, cron, systemd

**Version Control:** Git, GitHub

## Security and Operational Considerations

- Private application instances are not directly exposed to the Internet.
- Application traffic between EC2 instances is controlled by Security Groups.
- Session Manager provides administrative access without inbound SSH.
- The demonstration's HTTP access was restricted to a specific client IP address.
- Production deployments should use HTTPS with valid TLS certificates, appropriate monitoring thresholds, and additional security controls.
- Temporary NAT Gateway and SSM Interface VPC Endpoints were deleted after testing to reduce costs.
- Stopped EC2 instances can still incur storage-related charges.

## Project Status

**Hands-on implementation and core operational tests completed.**

This project demonstrates a two-tier AWS application with Linux service automation, private networking, reverse proxy routing, CloudWatch monitoring, and verified troubleshooting scenarios.

It is a learning and portfolio project, not a production-ready deployment.
