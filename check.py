import os
import requests
import sys

url = os.getenv("TARGET_URL")
if not url:
    print("Please set the TARGET_URL environment variable.")
    sys.exit(1)

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; GitHubActions/1.0)"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    print(f"Status code: {response.status_code}")
    if response.status_code == 403:
        print("Access forbidden – possible block on GitHub runner.")
    elif response.status_code == 200:
        print("Access OK – no blocking detected.")
    else:
        print(f"Received status code {response.status_code} – check manually.")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
