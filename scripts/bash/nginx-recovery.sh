#!/bin/bash

if systemctl is-active --quiet nginx; then
    echo "HEALTHY: Nginx is running"
else
    echo "ALERT: Nginx is stopped. Attempting recovery..."

    if sudo systemctl start nginx &&
       systemctl is-active --quiet nginx; then
        echo "RECOVERED: Nginx is running again"
    else
        echo "CRITICAL: Automatic recovery failed"
        exit 1
    fi
fi
