#!/usr/bin/env python3
"""dblog: show recent 3kdb changes in game, read straight from git history.

The log comes from the upstream master branch (jmitchell33/3kdb), so only work
that was merged or pushed there shows. Branch work, WIP and discarded code never
reach master, so they never show. A revert hides both itself and the commit it
undoes. Character files (chars/) and saved settings (vars/) are ignored: a
commit that only touched those is hidden.

Output is TinTin++ colour-coded text, one line per row, read by common/dblog.tin.
"""

import argparse
import os
import re
import subprocess
import sys
import textwrap

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEEN_FILE = os.path.join(REPO, "vars", "dblog_seen.txt")
UPSTREAM_URL = "jmitchell33/3kdb"
BRANCHES = ("master", "main")
IGNORED_DIRS = ("chars/", "vars/", "logs/")
TRAILER = re.compile(
    r"^(co-authored-by|signed-off-by|reviewed-by|\(cherry picked from)", re.IGNORECASE
)
REVERTS = re.compile(r"This reverts commit ([0-9a-f]{7,40})")
SYNC_MERGE = re.compile(r"^Merge (branch|remote-tracking branch) ")
SINCE_SHORT = re.compile(r"^(\d+)([dwmy])$")
SINCE_UNITS = {"d": "days", "w": "weeks", "m": "months", "y": "years"}
SEP_REC, SEP_FLD, SEP_END = "\x1e", "\x1f", "\x1d"

C_HEAD = "<ccf>"
C_DATE = "<eaf>"
C_HASH = "<bca>"
C_NAME = "<ceb>"
C_TEXT = "<fff>"
C_NEW = "<ffa>"
C_DIM = "<ccc>"
C_CMD = "<eaf>"
C_WARN = "<eed>"
C_END = "<088>"


class Commit:
    def __init__(self, full, short, author, date, subject, body, files):
        self.full = full
        self.short = short
        self.author = author
        self.date = date
        self.subject = subject
        self.body = body
        self.files = files


def git(*args, timeout=30):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    result = subprocess.run(
        ["git", "-C", REPO, *args],
        capture_output=True, text=True, timeout=timeout,
        encoding="utf-8", errors="replace", env=env,
    )
    return result.returncode, result.stdout


def safe(text):
    """Keep commit text from being read as TinTin++ code or colour codes."""
    text = text.replace("{", "(").replace("}", ")").replace("\\", "/")
    return re.sub(r"<([0-9a-fA-F]{3}|[a-zA-Z][0-9a-zA-Z]{2})>", r"(\1)", text)


def find_upstream_ref():
    """Return (remote, branch, ref) for upstream master, else HEAD."""
    code, out = git("remote")
    remotes = out.split() if code == 0 else []
    ranked = [r for r in remotes if UPSTREAM_URL in remote_url(r)]
    ranked += [r for r in ("upstream", "origin") if r in remotes and r not in ranked]
    for remote in ranked:
        for branch in BRANCHES:
            ref = f"{remote}/{branch}"
            if git("rev-parse", "--verify", "--quiet", ref)[0] == 0:
                return remote, branch, ref
    return None, None, "HEAD"


def remote_url(name):
    code, out = git("remote", "get-url", name)
    return out.strip() if code == 0 else ""


def shown_files(files):
    return [f for f in files if not f.startswith(IGNORED_DIRS)]


def clean_body(body):
    lines = []
    for line in body.splitlines():
        if TRAILER.match(line.strip()) or "chars/" in line:
            continue
        lines.append(line.rstrip())
    while lines and not lines[-1]:
        lines.pop()
    while lines and not lines[0]:
        lines.pop(0)
    return lines


def read_commits(rev_range):
    fmt = SEP_REC + SEP_FLD.join(["%H", "%h", "%an", "%ad", "%s", "%b"]) + SEP_END
    args = ["log", "--no-merges", "--date=short", "--name-only", f"--format={fmt}"]
    code, out = git(*args, rev_range, "--")
    if code != 0:
        return None
    commits = []
    for record in out.split(SEP_REC)[1:]:
        head, _, tail = record.partition(SEP_END)
        fields = head.split(SEP_FLD)
        if len(fields) < 6:
            continue
        files = [f for f in tail.split("\n") if f.strip()]
        commits.append(Commit(*fields[:6], files))
    return drop_hidden(commits)


def drop_hidden(commits):
    """Drop reverted pairs, character-only commits and merge syncs."""
    reverted = set()
    for c in commits:
        match = REVERTS.search(c.body)
        if match:
            reverted.add(match.group(1))
            reverted.add(c.full)
    kept = []
    for c in commits:
        if c.full in reverted or any(c.full.startswith(r) for r in reverted if len(r) < 40):
            continue
        if SYNC_MERGE.match(c.subject):
            continue
        c.files = shown_files(c.files)
        if not c.files:
            continue
        c.body = clean_body(c.body)
        kept.append(c)
    return kept


def since_arg(word):
    match = SINCE_SHORT.match(word)
    if match:
        return f"{match.group(1)} {SINCE_UNITS[match.group(2)]} ago"
    if word in ("today", "yesterday"):
        return "1 days ago" if word == "today" else "2 days ago"
    if word in ("week", "month", "year"):
        return f"1 {word}s ago"
    return word


def parse_query(words):
    query = {"limit": None, "all": False, "by": [], "file": [], "since": None,
             "words": [], "mode": "list", "target": None, "since_set": None}
    i = 0
    while i < len(words):
        word = words[i]
        low = word.lower()
        nxt = words[i + 1] if i + 1 < len(words) else None
        if low in ("help", "?"):
            query["mode"] = "help"
        elif low == "new":
            query["mode"] = "new"
        elif low == "show" and nxt:
            query["mode"], query["target"] = "show", nxt
            i += 1
        elif low == "all":
            query["all"] = True
        elif low.isdigit():
            query["limit"] = int(low)
        elif low in ("by", "file", "since") and nxt:
            if low == "since":
                query["since"] = since_arg(nxt.lower())
            else:
                query[low].append(nxt.lower())
            i += 1
        else:
            query["words"].append(low)
        i += 1
    return query


def since_hashes(ref, since):
    code, out = git("rev-list", f"--since={since}", ref)
    return set(out.split()) if code == 0 else set()


def matches(c, query):
    if query["since_set"] is not None and c.full not in query["since_set"]:
        return False
    if any(b not in c.author.lower() for b in query["by"]):
        return False
    paths = [f.lower() for f in c.files]
    if any(not any(p in f for f in paths) for p in query["file"]):
        return False
    haystack = " ".join([c.subject, *c.body, c.author, *c.files, c.short]).lower()
    return all(w in haystack for w in query["words"])


def read_seen():
    try:
        with open(SEEN_FILE, encoding="utf-8") as handle:
            return handle.read().strip()
    except OSError:
        return ""


def write_seen(full_hash):
    try:
        os.makedirs(os.path.dirname(SEEN_FILE), exist_ok=True)
        with open(SEEN_FILE, "w", encoding="utf-8") as handle:
            handle.write(full_hash + "\n")
    except OSError:
        pass


def unseen_count(commits, seen):
    """Changes above the last one seen; 0 if it's gone from the history."""
    for index, c in enumerate(commits):
        if c.full == seen:
            return index
    return 0


def not_pulled(ref):
    if ref == "HEAD":
        return set()
    code, out = git("rev-list", f"HEAD..{ref}")
    return set(out.split()) if code == 0 else set()


def wrap(text, width, indent):
    return textwrap.wrap(text, width=max(width - indent, 20)) or [""]


def entry_lines(c, cols, new, pending, full_body=False):
    mark = f"{C_NEW}*{C_END}" if new else " "
    tag = f" {C_WARN}(not pulled){C_END}" if c.full in pending else ""
    lead = f" {mark} {C_DATE}{c.date}{C_END} {C_HASH}{c.short}{C_END} "
    lead_len = 3 + len(c.date) + 1 + len(c.short) + 1
    tail = f" {C_DIM}- {safe(c.author)}{C_END}"
    lines = wrap(safe(c.subject), cols - len(c.author) - 3, lead_len)
    out = [f"{lead}{C_TEXT}{lines[0]}{C_END}" + (tail if len(lines) == 1 else "")]
    for index, part in enumerate(lines[1:], 2):
        end = tail if index == len(lines) else ""
        out.append(" " * lead_len + f"{C_TEXT}{part}{C_END}{end}")
    if tag:
        out[-1] += tag
    if full_body:
        for para in c.body:
            for part in wrap(safe(para), cols, 4) if para else [""]:
                out.append(f"    {C_NAME}{part}{C_END}")
    return out


def header(title):
    return [f"{C_HEAD}  -------    {C_NEW}3kdb {title}{C_HEAD}    -------{C_END}", ""]


def print_lines(lines):
    sys.stdout.write("\n".join(lines) + "\n")


def show_help():
    rows = [
        ("dblog", "the latest 10 changes"),
        ("dblog more", "the next page of the last search"),
        ("dblog 25", "the latest 25"),
        ("dblog all", "every change"),
        ("dblog <words>", "changes mentioning all the words: dblog map hell"),
        ("dblog file <part>", "changes to matching files: dblog file westersea"),
        ("dblog by <name>", "changes by an author: dblog by karvec"),
        ("dblog since <when>", "7d 2w 3m 1y, week, month or 2026-11-01"),
        ("dblog show <hash>", "the full write-up and files of one change"),
        ("dblog new", "check GitHub for changes you haven't pulled yet"),
    ]
    lines = header("CHANGE LOG HELP")
    for name, desc in rows:
        lines.append(f"  {C_NAME}{name:<20}{C_END}  {C_TEXT}{safe(desc)}{C_END}")
    lines += ["", f"  {C_DIM}Mix them: dblog by karvec file map 20 or dblog bot all{C_END}",
              f"  {C_NEW}*{C_DIM} marks changes you haven't seen in dblog yet.{C_END}"]
    print_lines(lines)


def show_one(commits, target, cols):
    target = target.lower()
    hits = [c for c in commits if c.full.startswith(target)]
    if not hits:
        print_lines([f"  {C_WARN}No change found with hash {safe(target)}.{C_END}"])
        return
    c = hits[0]
    lines = header("CHANGE " + c.short)
    lines += entry_lines(c, cols, False, set(), full_body=True)
    lines += ["", f"    {C_HEAD}Files ({len(c.files)}):{C_END}"]
    lines += [f"      {C_DIM}{safe(f)}{C_END}" for f in c.files]
    print_lines(lines)


def list_changes(commits, query, args, ref):
    seen = read_seen()
    fresh = unseen_count(commits, seen)
    new_hashes = {c.full for c in commits[:fresh]}
    filtered = bool(query["words"] or query["by"] or query["file"] or query["since"])
    hits = [c for c in commits if matches(c, query)]
    limit = query["limit"] or args.count
    page = hits[args.skip:] if query["all"] else hits[args.skip:args.skip + limit]
    pending = not_pulled(ref)

    lines = header("RECENT CHANGES" if not filtered else "CHANGES FOUND")
    if fresh and not filtered and args.skip == 0:
        lines.insert(1, f"  {C_NEW}{fresh} new since you last looked.{C_END}")
    if not page:
        lines.append(f"  {C_WARN}No changes found.{C_END}")
    for c in page:
        lines += entry_lines(c, args.cols, c.full in new_hashes, pending)
    shown_to = args.skip + len(page)
    lines.append("")
    if page:
        lines.append(f"  {C_HEAD}Showing {args.skip + 1}-{shown_to} of {len(hits)}.{C_END}")
    more = shown_to < len(hits)
    hints = (["dblog more"] if more else []) + ["dblog show <hash>", "dblog help"]
    bar = f"{C_HEAD}  |  "
    lines.append("  " + bar.join(f"{C_CMD}{h}" for h in hints) + C_END)
    print_lines(lines)
    print(f"#DBLOG_MORE {1 if more else 0} {shown_to}")
    if commits and args.skip == 0 and not filtered:
        write_seen(commits[0].full)


def show_new(cols):
    remote, branch, ref = find_upstream_ref()
    if not remote:
        print_lines([f"  {C_WARN}No GitHub remote found for this folder.{C_END}"])
        return
    try:
        code, _ = git("fetch", "--quiet", remote, branch, timeout=25)
    except subprocess.TimeoutExpired:
        code = 1
    if code != 0:
        print_lines([f"  {C_WARN}Couldn't reach GitHub, showing what was last fetched.{C_END}"])
    commits = read_commits(f"HEAD..{ref}") or []
    lines = header("CHANGES TO PULL")
    if not commits:
        lines.append(f"  {C_TEXT}You're up to date.{C_END}")
    for c in commits:
        lines += entry_lines(c, cols, False, set())
    if commits:
        lines += ["", f"  {C_HEAD}{len(commits)} to get. Quit tt++ and run "
                      f"{C_NEW}git pull{C_HEAD} in the 3kdb folder.{C_END}"]
    print_lines(lines)


def login_notice():
    _, _, ref = find_upstream_ref()
    commits = read_commits(ref) or []
    if not commits:
        return
    seen = read_seen()
    if not seen:
        write_seen(commits[0].full)
        return
    fresh = unseen_count(commits, seen)
    if not fresh and seen != commits[0].full and seen not in {c.full for c in commits}:
        write_seen(commits[0].full)
    if fresh:
        word = "change" if fresh == 1 else "changes"
        print(f"{C_NEW}3kdb:{C_TEXT} {fresh} new {word} since you last looked. "
              f"Type {C_NAME}dblog{C_TEXT} to see them.{C_END}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cols", type=int, default=100)
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--skip", type=int, default=0)
    parser.add_argument("--login", action="store_true")
    parser.add_argument("query", nargs="*")
    args = parser.parse_args()
    args.count = max(args.count, 1)
    args.cols = max(args.cols, 60)

    if git("rev-parse", "--git-dir")[0] != 0:
        if not args.login:
            print_lines([f"  {C_WARN}dblog needs 3kdb installed with git clone.{C_END}"])
        return
    if args.login:
        login_notice()
        return
    query = parse_query(" ".join(args.query).split())
    if query["mode"] == "help":
        show_help()
        return
    if query["mode"] == "new":
        show_new(args.cols)
        return
    _, _, ref = find_upstream_ref()
    commits = read_commits(ref)
    if commits is None:
        print_lines([f"  {C_WARN}Couldn't read the git history.{C_END}"])
        return
    if query["mode"] == "show":
        show_one(commits, query["target"], args.cols)
        return
    if query["since"]:
        query["since_set"] = since_hashes(ref, query["since"])
    list_changes(commits, query, args, ref)


if __name__ == "__main__":
    main()
