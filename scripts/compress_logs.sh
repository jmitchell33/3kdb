#!/bin/sh
# Compress finished daily logs under a folder with zstd. With a size cap, also delete the
# oldest compressed logs until the folder is under it; with no cap (or 0) nothing is deleted.
#
#   sh scripts/compress_logs.sh <folder> [cap in MB]
#
# A log is finished when its name ends in a date before today (..._YYYY-MM-DD.log or
# YYYY-MM-DD.log) and nothing has written to it for 10 minutes. Read compressed logs with
# zstdless, zstdcat or zstdgrep.
#
# zstd -9 makes 3k logs about 15x smaller using ~64 MB of memory. Don't swap in xz -9: it
# needs ~700 MB and got killed for running out of memory on a 1 GB box.

dir=$1
cap_mb=${2:-0}
[ -d "$dir" ] || exit 1

# Every game session runs this when it starts and when the day changes, so only one at a time
exec 9>"$dir/.compress_logs.lock"
flock -n 9 || exit 0

today=$(date +%Y-%m-%d)

find "$dir" -type f -name '*.log' -mmin +10 | while read -r f; do
    day=$(basename "$f" .log | grep -o '[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}$') || continue
    [ "$day" \< "$today" ] || continue
    # --rm only deletes the log once the .zst is written
    nice -n 19 zstd -q -9 --rm "$f"
done

# Oldest compressed logs go first. Uncompressed logs (today's) are never deleted
[ "$cap_mb" -gt 0 ] || exit 0
while [ "$(du -sm "$dir" | cut -f1)" -gt "$cap_mb" ]; do
    oldest=$(find "$dir" -type f -name '*.zst' -printf '%T@ %p\n' | sort -n | head -1 | cut -d' ' -f2-)
    [ -n "$oldest" ] || break
    rm -f "$oldest"
done
