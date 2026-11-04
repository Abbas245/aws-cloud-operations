
# AWS Cloud Operations — Architecture

## Network

- Region: us-east-1
- VPC: 10.0.0.0/16
- Public subnet: 10.0.1.0/24
- Private subnet: 10.0.2.0/24
- Internet Gateway: Connected to public routing
- Private route table: Local VPC routing only

## Public Web Server

- Ubuntu 24.04 EC2
- Nginx serving a static website
- Bash health monitoring and recovery
- Reverse proxy forwarding `/app/` to the private application

## Private Application Server

- Ubuntu 24.04 EC2
- Python HTTP application on port 8080
- No public IPv4 address
- Inbound TCP 8080 permitted from the Web EC2 Security Group
- systemd automatic startup and process recovery

## Monitoring

- Amazon CloudWatch EC2 CPU metrics
- CPU alarm threshold: Greater than 10%
- Evaluation: 1 out of 1 five-minute periods
- Alarm transitions verified during controlled CPU load testing

## Verified Tests

- Web EC2 to Private App EC2 connectivity
- Nginx reverse proxy returned HTTP 200
- Backend stopped: Nginx returned HTTP 502
- Backend restored: Nginx returned HTTP 200
- Python process crash: systemd restarted the service
- EC2 reboot: Python application started automatically
- CloudWatch CPU alarm entered ALARM and returned to OK
- Private EC2 accessed through temporary SSM Interface VPC Endpoints without NAT

## Cleanup

The temporary NAT Gateway and SSM Interface VPC Endpoints were deleted after testing. The EC2 instances can be stopped when not in use.
