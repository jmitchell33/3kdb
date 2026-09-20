import sys, requests, time
from datetime import datetime, timedelta, timezone

def parse_cooldown(value):
    if value is None or value == "RDY" or (isinstance(value, str) and "xB" in value):
        return None
    now = datetime.now(timezone.utc)
    try:
        if value.endswith("m"):
            return (now + timedelta(minutes=float(value[:-1]))).isoformat()
        elif value.endswith("h"):
            return (now + timedelta(hours=float(value[:-1]))).isoformat()
        elif value.endswith("D"):
            return (now + timedelta(days=float(value[:-1]))).isoformat()
    except (ValueError, AttributeError):
        pass
    return None


url = str(sys.argv[1])
data = ""
for i in range(len(sys.argv)):
    if i >= 2:
        data = " ".join([data, sys.argv[i]])

headers = {'Content-Type': "application/json", 'Accept': "application/json"}

data = data.replace("x7B", "{")
data = data.replace("x7D", "}")
parsed = {}
for pair in data.strip().split(","):
    if ":" not in pair:
        continue
    k, v = pair.split(":", 1)
    k, v = k.strip().replace(" ", "_"), v.strip()
    if v == "true":
        parsed[k] = True
    elif v == "false":
        parsed[k] = False
    elif v == "null":
        parsed[k] = None
    else:
        parsed[k] = v

for k in list(parsed.keys()):
    if k.startswith("cooldown_"):
        parsed[k] = parse_cooldown(parsed[k])

data = parsed

try:
    res = requests.post(url, json=data, headers=headers)
    print(f"{res.status_code} {res.text}")
except requests.exceptions.SSLError:
    time.sleep(3)
    try:
        res = requests.post(url, json=data, headers=headers)
        print(f"{res.status_code} {res.text}")
    except Exception as e:
        print(f"SSL error: {e}")
except Exception as e:
    print(f"Error: {e}")
