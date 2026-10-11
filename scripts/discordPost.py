import fcntl
import json
import os
import sys
import time

import requests

# Discord allows 2000 characters per message
MAX_LEN = 2000


def log(msg):
    print(time.strftime("%Y-%m-%d %H:%M:%S ") + msg, flush=True)


if len(sys.argv) < 2:
    log("Error: No file path provided")
    sys.exit(1)

path = sys.argv[1]
try:
    with open(path, 'r') as f:
        obj = json.loads(f.read())
except FileNotFoundError:
    log(f"Error: File not found: {path}")
    sys.exit(1)
except json.JSONDecodeError as e:
    log(f"Error: Invalid JSON: {e}")
    sys.exit(1)
finally:
    if os.path.exists(path):
        os.remove(path)

# tintin starts each batch in the background, so wait for any earlier batch to
# finish first. That keeps messages in order and the batches from racing each
# other into the rate limit
lock = open(os.path.join(os.path.dirname(path) or ".", "discordPost.lock"), "w")
fcntl.flock(lock, fcntl.LOCK_EX)

# Join each channel's lines into as few messages as fit, so a busy batch is a
# handful of requests instead of one per line
messages = {}
for key in obj:
    try:
        url = obj[key]["channel"]
        text = obj[key]["payload"]
    except KeyError as e:
        log(f"Error on entry {key}: Missing field {e}")
        continue
    chunks = messages.setdefault(url, [""])
    if chunks[-1] and len(chunks[-1]) + 1 + len(text) > MAX_LEN:
        chunks.append("")
    chunks[-1] = f"{chunks[-1]}\n{text}" if chunks[-1] else text[:MAX_LEN]

headers = {"Content-Type": "application/json", "Accept": "application/json"}
for url, chunks in messages.items():
    for content in chunks:
        # Retry when Discord says to slow down, waiting as long as it asks
        for attempt in range(5):
            try:
                res = requests.post(url, json={"content": content}, headers=headers, timeout=10)
            except requests.exceptions.Timeout:
                log("Error: Request timed out")
                break
            except requests.exceptions.ConnectionError as e:
                log(f"Error: Connection error - {e}")
                break
            if res.status_code == 429:
                try:
                    wait = float(res.json().get("retry_after", 1))
                except ValueError:
                    wait = 1
                time.sleep(wait)
                continue
            if res.status_code not in (200, 204):
                log(f"Error: HTTP {res.status_code} - {res.text}")
            break
        else:
            log("Error: Still rate limited after 5 tries, dropped a message")
