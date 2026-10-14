import fcntl
import json
import os
import re
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
# chatlog.tin writes one message per line as "channel<tab>text". Older batches
# were a JSON object of {"n": {"channel": ..., "payload": ...}}, still accepted
try:
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        raw = f.read()
except FileNotFoundError:
    log(f"Error: File not found: {path}")
    sys.exit(1)
finally:
    if os.path.exists(path):
        os.remove(path)

if raw.lstrip().startswith('{'):
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError as e:
        log(f"Error: Invalid JSON: {e}")
        sys.exit(1)
else:
    obj = {}
    for n, line in enumerate(raw.splitlines(), 1):
        url, sep, text = line.partition('\t')
        if not sep or not url:
            log(f"Error on line {n}: expected channel<tab>text")
            continue
        obj[str(n)] = {"channel": url, "payload": text}

# tintin starts each batch in the background, so wait for any earlier batch to
# finish first. That keeps messages in order and the batches from racing each
# other into the rate limit
lock = open(os.path.join(os.path.dirname(path) or ".", "discordPost.lock"), "w")
fcntl.flock(lock, fcntl.LOCK_EX)

# Show chat text as typed: escape Discord formatting (*bold*, _italic_, `code`,
# ~~strike~~, ||spoiler||) and don't let @everyone, @here or user mentions ping
MARKDOWN = re.compile(r'([\\*_~`|])')
NO_PINGS = {"parse": []}

# Join each channel's lines into as few messages as fit, so a busy batch is a
# handful of requests instead of one per line
messages = {}
for key in obj:
    try:
        url = obj[key]["channel"]
        # chatlog.tin swaps backslashes and semicolons for the look-alikes U+FF3C
        # and U+FF1B, so swap them back
        payload = obj[key]["payload"].replace("\uff3c", "\\").replace("\uff1b", ";")
        text = MARKDOWN.sub(r'\\\1', payload)
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
                res = requests.post(url, json={"content": content, "allowed_mentions": NO_PINGS}, headers=headers, timeout=10)
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
