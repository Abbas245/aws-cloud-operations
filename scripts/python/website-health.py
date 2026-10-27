import sys
import urllib.request

url = "http://localhost"

try:
    with urllib.request.urlopen(url, timeout=5) as response:
        if response.status == 200:
            print("HEALTHY: Website returned HTTP 200")
            sys.exit(0)
        else:
            print(f"UNHEALTHY: HTTP {response.status}")
            sys.exit(1)

except Exception as error:
    print(f"UNHEALTHY: {error}")
    sys.exit(1)
