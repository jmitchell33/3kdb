import sys
import json
import requests

if len(sys.argv) < 2:
    print("Error: No file path provided", flush=True)
    sys.exit(1)

try:
    with open(sys.argv[1], 'r') as f:
        obj = json.loads(f.read())
except FileNotFoundError:
    print(f"Error: File not found: {sys.argv[1]}", flush=True)
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON: {e}", flush=True)
    sys.exit(1)

for key in obj:
    try:
        url = obj[key]["channel"]
        payload = {"content": obj[key]["payload"]}
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        res = requests.post(url, json=payload, headers=headers, timeout=10)
        if res.status_code not in (200, 204):
            print(f"Error on entry {key}: HTTP {res.status_code} - {res.text}", flush=True)
    except requests.exceptions.Timeout:
        print(f"Error on entry {key}: Request timed out", flush=True)
    except requests.exceptions.ConnectionError as e:
        print(f"Error on entry {key}: Connection error - {e}", flush=True)
    except KeyError as e:
        print(f"Error on entry {key}: Missing field {e}", flush=True)