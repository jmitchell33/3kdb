#!/usr/bin/env python3
"""dblog: show recent 3kdb changes in game, read straight from git history.

The log comes from the upstream master branch (jmitchell33/3kdb), so only work
that was merged or pushed there shows. Branch work, WIP and discarded code never
reach master, so they never show. A revert hides both itself and the commit it
undoes. Character files (chars/) and saved settings (vars/) are ignored: a
commit that only touched those is hidden.

Where the history comes from, first that works:
  1. this 3kdb folder, when it's a git clone (its upstream or origin master)
  2. a small copy of the GitHub history in vars/dblog_cache.git, when git is
     installed but this folder isn't a clone (a zip download, a copy, or git
     refusing a folder owned by another user)
  3. the GitHub website, when git isn't installed at all

Output is TinTin++ colour-coded text, one line per row, read by common/dblog.tin.
"""

import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
import time
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEEN_FILE = os.path.join(REPO, "vars", "dblog_seen.txt")
UPSTREAM_URL = "jmitchell33/3kdb"
CLONE_URL = f"https://github.com/{UPSTREAM_URL}.git"
API_URL = f"https://api.github.com/repos/{UPSTREAM_URL}"
CACHE_GIT = os.path.join(REPO, "vars", "dblog_cache.git")
CACHE_JSON = os.path.join(REPO, "vars", "dblog_cache.json")
CACHE_MAX_AGE = 30 * 60
API_PAGES = 3
API_DETAIL_CALLS = 20
BRANCHES = ("master", "main")
IGNORED_DIRS = ("chars/", "vars/", "logs/")
TRAILER = re.compile(
    r"^(co-authored-by|signed-off-by|reviewed-by|\(cherry picked from)", re.IGNORECASE
)
REVERTS = re.compile(r"This reverts commit ([0-9a-f]{7,40})")
SYNC_MERGE = re.compile(r"^Merge (branch|remote-tracking branch) ")
SINCE_SHORT = re.compile(r"^(\d+)([dwmy])$")
SINCE_DAYS = {"d": 1, "w": 7, "m": 30, "y": 365}
SINCE_WORDS = {"today": 0, "yesterday": 1, "week": 7, "month": 30, "year": 365}
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


# Where git commands point: this folder, or the history copy in vars/ (use_cache)
GIT_TARGET = ["-c", f"safe.directory={REPO}", "-C", REPO]
INSTALLED = True


def git(*args, timeout=30):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    try:
        result = subprocess.run(
            ["git", *GIT_TARGET, *args],
            capture_output=True, text=True, timeout=timeout,
            encoding="utf-8", errors="replace", env=env,
        )
    except (OSError, subprocess.TimeoutExpired):
        return 1, ""
    return result.returncode, result.stdout


def have_git():
    try:
        subprocess.run(["git", "--version"], capture_output=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return False
    return True


def use_cache():
    global GIT_TARGET, INSTALLED
    GIT_TARGET = ["--git-dir", CACHE_GIT]
    INSTALLED = False


def cache_age():
    try:
        return time.time() - os.path.getmtime(os.path.join(CACHE_GIT, "dblog_fetched"))
    except OSError:
        return None


def mark_fetched():
    try:
        with open(os.path.join(CACHE_GIT, "dblog_fetched"), "w", encoding="utf-8"):
            pass
    except OSError:
        pass


def clone_cache():
    """Copy the upstream master history (no file contents) into vars/dblog_cache.git."""
    os.makedirs(os.path.dirname(CACHE_GIT), exist_ok=True)
    temp = f"{CACHE_GIT}.part{os.getpid()}"
    shutil.rmtree(temp, ignore_errors=True)
    code, _ = git("clone", "--quiet", "--bare", "--filter=blob:none", "--single-branch",
                  "--branch", "master", CLONE_URL, temp, timeout=90)
    if code != 0:
        shutil.rmtree(temp, ignore_errors=True)
        return False
    try:
        os.rename(temp, CACHE_GIT)
    except OSError:
        shutil.rmtree(temp, ignore_errors=True)
    mark_fetched()
    return os.path.isdir(CACHE_GIT)


def refresh_cache(force=False):
    """Fetch master into the history copy when it's older than CACHE_MAX_AGE (or force)."""
    age = cache_age()
    if not force and age is not None and age < CACHE_MAX_AGE:
        return True
    code, _ = git("fetch", "--quiet", CLONE_URL, "+refs/heads/master:refs/heads/master",
                  timeout=60)
    if code == 0:
        mark_fetched()
    return code == 0


def pick_source(fetch=False):
    """Return the ref to read, or None for the GitHub website. fetch: get the latest now."""
    if git("rev-parse", "--git-dir")[0] == 0:
        return find_upstream_ref()[2]
    if not have_git():
        return None
    if not os.path.isdir(CACHE_GIT):
        GIT_TARGET[:] = []
        if not clone_cache():
            use_cache()
            return None
        use_cache()
        return "master"
    use_cache()
    refresh_cache(force=fetch)
    return "master"


def api_get(path):
    request = urllib.request.Request(
        f"{API_URL}/{path}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "3kdb-dblog"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def read_api_cache():
    try:
        with open(CACHE_JSON, encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, ValueError):
        return {}


def write_api_cache(cache):
    try:
        os.makedirs(os.path.dirname(CACHE_JSON), exist_ok=True)
        with open(CACHE_JSON + ".part", "w", encoding="utf-8") as handle:
            json.dump(cache, handle)
        os.replace(CACHE_JSON + ".part", CACHE_JSON)
    except OSError:
        pass


def api_commit(item):
    info = item["commit"]
    subject, _, body = info["message"].partition("\n")
    return {"full": item["sha"], "short": item["sha"][:7], "author": info["author"]["name"],
            "date": info["author"]["date"][:10], "subject": subject,
            "body": body.lstrip("\n"), "parents": len(item.get("parents", []))}


def api_list(cache, fetch):
    """The newest master commits from GitHub, kept in vars/dblog_cache.json between runs."""
    fresh = time.time() - cache.get("fetched", 0) < CACHE_MAX_AGE
    if cache.get("commits") and fresh and not fetch:
        return cache["commits"]
    commits = []
    try:
        for page in range(1, API_PAGES + 1):
            items = api_get(f"commits?sha=master&per_page=100&page={page}")
            commits += [api_commit(item) for item in items]
            if len(items) < 100:
                break
    except (OSError, ValueError, KeyError):
        return cache.get("commits")
    cache["commits"] = commits
    cache["fetched"] = time.time()
    return commits


def api_files(cache, full, budget):
    """Files one commit changed, asked of GitHub once and then kept in the cache."""
    files = cache.setdefault("files", {})
    if full not in files and budget[0] > 0:
        budget[0] -= 1
        try:
            files[full] = [f["filename"] for f in api_get(f"commits/{full}").get("files", [])]
        except (OSError, ValueError, KeyError):
            budget[0] = 0
    return files.get(full)


def read_api_commits(fetch=False, need=None):
    """Commits from the GitHub website. need: how many from the top must have file lists."""
    cache = read_api_cache()
    raw = api_list(cache, fetch)
    if raw is None:
        return None
    budget = [API_DETAIL_CALLS]
    commits = []
    for entry in raw:
        if entry["parents"] > 1:
            continue
        wanted = need is None or len(commits) < need
        files = api_files(cache, entry["full"], budget) if wanted else None
        commit = Commit(entry["full"], entry["short"], entry["author"], entry["date"],
                        entry["subject"], entry["body"], files)
        if files is not None and not shown_files(files):
            continue
        commits.append(commit)
    write_api_cache(cache)
    return drop_hidden(commits)


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
    args = ["log", "--no-merges", "--no-renames", "--date=short", "--name-only",
            f"--format={fmt}"]
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
        if c.files is not None:
            c.files = shown_files(c.files)
            if not c.files:
                continue
        c.body = clean_body(c.body)
        kept.append(c)
    return kept


def since_arg(word):
    """The first date (YYYY-MM-DD) for since: 7d 2w 3m 1y, today, week or 2026-11-01."""
    today = datetime.date.today()
    match = SINCE_SHORT.match(word)
    if match:
        days = int(match.group(1)) * SINCE_DAYS[match.group(2)]
    elif word in SINCE_WORDS:
        days = SINCE_WORDS[word]
    else:
        try:
            return datetime.date.fromisoformat(word).isoformat()
        except ValueError:
            return ""
    return (today - datetime.timedelta(days=days)).isoformat()


def parse_query(words):
    query = {"limit": None, "all": False, "by": [], "file": [], "since": None,
             "words": [], "mode": "list", "target": None}
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


def matches(c, query):
    if query["since"] is not None and c.date < query["since"]:
        return False
    if any(b not in c.author.lower() for b in query["by"]):
        return False
    paths = [f.lower() for f in c.files or []]
    if any(not any(p in f for f in paths) for p in query["file"]):
        return False
    haystack = " ".join([c.subject, *c.body, c.author, *(c.files or []), c.short]).lower()
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
    if ref in ("HEAD", None) or not INSTALLED:
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
    if c.files is None:
        cache = read_api_cache()
        files = api_files(cache, c.full, [1])
        write_api_cache(cache)
        c.files = shown_files(files) if files is not None else None
    lines = header("CHANGE " + c.short)
    lines += entry_lines(c, cols, False, set(), full_body=True)
    if c.files is not None:
        lines += ["", f"    {C_HEAD}Files ({len(c.files)}):{C_END}"]
        lines += [f"      {C_DIM}{safe(f)}{C_END}" for f in c.files]
    print_lines(lines)


def list_changes(commits, query, args, ref):
    seen = read_seen()
    fresh = unseen_count(commits, seen)
    new_hashes = {c.full for c in commits[:fresh]}
    filtered = bool(query["words"] or query["by"] or query["file"] or query["since"] is not None)
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
    if git("rev-parse", "--git-dir")[0] != 0:
        show_new_uninstalled(cols)
        return
    remote, branch, ref = find_upstream_ref()
    if not remote:
        print_lines([f"  {C_WARN}No GitHub remote found for this folder.{C_END}"])
        return
    code, _ = git("fetch", "--quiet", remote, branch, timeout=25)
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


def show_new_uninstalled(cols):
    """Not a git clone, so there's nothing to compare: show what's new since dblog last looked."""
    commits = load_commits(fetch=True, need=10)
    if commits is None:
        print_lines([f"  {C_WARN}Couldn't reach GitHub.{C_END}"])
        return
    fresh = unseen_count(commits, read_seen())
    lines = header("NEW ON GITHUB")
    if not fresh:
        lines.append(f"  {C_TEXT}Nothing new since you last looked.{C_END}")
    for c in commits[:fresh]:
        lines += entry_lines(c, cols, True, set())
    lines += ["", f"  {C_DIM}This 3kdb folder isn't a git clone, so dblog can't tell which of "
                  f"these you already have.{C_END}"]
    print_lines(lines)


def load_commits(fetch=False, need=None):
    """The upstream history from the best source there is (see the top of this file)."""
    ref = pick_source(fetch)
    if ref is None:
        return read_api_commits(fetch, need)
    return read_commits(ref)


def login_notice():
    commits = load_commits(need=10) or []
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
    if query["since"] == "":
        print_lines([f"  {C_WARN}since takes 7d 2w 3m 1y, week, month or 2026-11-01.{C_END}"])
        return
    need = None if query["all"] else args.skip + (query["limit"] or args.count)
    if query["mode"] == "show":
        need = 0
    ref = pick_source()
    commits = read_api_commits(need=need) if ref is None else read_commits(ref)
    if commits is None:
        print_lines([f"  {C_WARN}Couldn't read the 3kdb history from git or GitHub.{C_END}"])
        return
    if query["mode"] == "show":
        show_one(commits, query["target"], args.cols)
        return
    list_changes(commits, query, args, ref)


if __name__ == "__main__":
    main()
