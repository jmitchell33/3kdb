import sys, requests, time, json

url = str(sys.argv[1])
raw = " ".join(sys.argv[2:]).strip()

data = []
for record in raw.split("~"):
    parts = record.split(",")
    if len(parts) < 4:
        continue
    # parts: character, component (may be multi-word), quality, quantity
    character = parts[0].strip()
    quantity = parts[-1].strip()
    quality = parts[-2].strip()
    component = ",".join(parts[1:-2]).strip()
    data.append(json.dumps({
        "character": character,
        "component": component,
        "component_quality": quality,
        "quantity": int(quantity),
    }))

headers = {'Content-Type': "application/json", 'Accept': "application/json"}

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
