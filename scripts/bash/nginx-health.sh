#!/bin/bash

if systemctl is-active --quiet nginx; then
    echo "HEALTHY: Nginx is running"
else
    echo "UNHEALTHY: Nginx is stopped"
fi
