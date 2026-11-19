#!/bin/sh
# dblog.sh: gets the 3kdb change history from GitHub with curl, for common/dblog.tin.
#
#   sh scripts/dblog.sh <job> list         the history, refreshed when it's 10 minutes old
#   sh scripts/dblog.sh <job> login        the same, for the line at login
#   sh scripts/dblog.sh <job> new          the history refreshed now, and what this folder has
#   sh scripts/dblog.sh <job> show <hash>  the history, with the files of that one change
#   sh scripts/dblog.sh <job> file <part>  the history, and the changes to files matching <part>
#   sh scripts/dblog.sh - check            ok, or the first file or folder dblog can't use, as
#                                          perm|<path>|<owner>|<you>|<folder of 3kdb>
#
# Run it from the 3kdb folder. It needs only sh, curl, awk and tar, which every Ubuntu, WSL
# and macOS has. tt++ starts it in the background, and it never asks anything, so it can't
# freeze the game.
#
# Where the history comes from, first that works:
#   1. GitHub's API (api.github.com), the latest 300 changes with their files
#   2. the list saved last time, topped up with github.com's feed of the newest 20 changes
#   3. github.com's feed alone, when nothing is saved yet
#   4. this folder's own git history, when it's a git clone and GitHub can't be reached
# When something fails, why_<job>.tsv says exactly what, for dblog.tin to explain.
#
# Everything goes in vars/dblog_data/, and the last file written is done_<job>.tsv, so
# dblog.tin reads finished files only:
#
#   commits.tsv       sha, date, author, subject, body, files (one change per line, newest first)
#   head_<job>.tsv    the commits this checkout has, when it's a git clone (new and list)
#   diff_<job>.tsv    the files that differ from GitHub's, when it isn't a git clone (new)
#   match_<job>.tsv   part and sha for each change to a matching file (file)
#   show_<job>.tsv    the hash, write-up lines and files of one change (show)
#   done_<job>.tsv    seen (the last change dblog showed), clone, source, reason, host,
#                     detail and age. clone is 1 for a git clone, 2 for one with no git
#                     installed, 0 for copied files. source is github, saved, feed, local or
#                     none. age is how many minutes old a saved list is
#
# GitHub's API lets one address ask 60 times an hour without logging in. A refresh asks 3
# times (at most every 10 minutes), plus once for each new change's file list, and the
# answers are kept, so normal use stays far under it. github.com's feed and file download
# don't count toward that.

# Bytes stay bytes in awk, tr and sort, so mawk and gawk give the same answer
LC_ALL=C
export LC_ALL

JOB="$1"
MODE="$2"
shift 2
DATA="vars/dblog_data"
REPO_PATH="jmitchell33/3kdb"
API="https://api.github.com/repos/$REPO_PATH"
FEED="https://github.com/$REPO_PATH/commits/master.atom"
TARBALL="https://github.com/$REPO_PATH/archive/refs/heads/master.tar.gz"
PAGES="1 2 3"
FILE_TOP=20
FILE_FETCHES=10
SOURCE="github"
WHY="$DATA/why_$JOB.tsv"

# check: every folder and file dblog writes has to belong to whoever runs tt++, or at least
# be readable and writable by them, like after tt++ was run once with sudo
if [ "$MODE" = "check" ]; then
    me=$(id -un 2>/dev/null || echo "$USER")
    for path in . vars "$DATA" "$DATA/files"; do
        mkdir -p "$path" 2>/dev/null
        if [ ! -d "$path" ] || [ ! -w "$path" ] || [ ! -x "$path" ]; then
            [ -d "$path" ] || path=$(dirname "$path")
            owner=$(ls -ld "$path" 2>/dev/null | awk '{ print $3 }')
            printf 'perm|%s|%s|%s|%s\n' "$path" "$owner" "$me" "$(pwd)"
            exit 0
        fi
    done
    for path in vars/dblog_seen.txt "$DATA"/* "$DATA"/files/*; do
        [ -e "$path" ] || continue
        if [ ! -r "$path" ] || [ ! -w "$path" ]; then
            owner=$(ls -ld "$path" 2>/dev/null | awk '{ print $3 }')
            printf 'perm|%s|%s|%s|%s\n' "$path" "$owner" "$me" "$(pwd)"
            exit 0
        fi
    done
    echo ok
    exit 0
fi

mkdir -p "$DATA/files" 2>/dev/null
# The old Python dblog's copies, and files from jobs tt++ stopped waiting for
rm -rf vars/dblog_cache.git vars/dblog_cache.json 2>/dev/null
find "$DATA" -maxdepth 1 \( -name '*_*.*' -o -name 'github_*' \) -mmin +10 \
    -exec rm -rf {} + 2>/dev/null

# Write the status file last, through a rename, so dblog.tin never reads half of it
finish() {
    seen=$(head -n 1 vars/dblog_seen.txt 2>/dev/null | tr -cd '0-9a-f')
    clone=0
    if [ -f "$DATA/head_$JOB.tsv" ]; then
        clone=1
    elif [ -e .git ]; then
        clone=2
    fi
    reason=""
    host=""
    detail=""
    if [ -f "$WHY" ]; then
        IFS="$(printf '\t')" read -r reason host detail < "$WHY"
    fi
    age=0
    if [ -f "$DATA/history.tsv" ]; then
        changed=$(stat -c %Y "$DATA/history.tsv" 2>/dev/null \
            || stat -f %m "$DATA/history.tsv" 2>/dev/null || date +%s)
        age=$(( ($(date +%s) - changed) / 60 ))
    fi
    printf 'seen\tclone\tsource\treason\thost\tdetail\tage\n' > "$DATA/done_$JOB.part"
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$seen" "$clone" "$SOURCE" "$reason" "$host" \
        "$detail" "$age" >> "$DATA/done_$JOB.part"
    mv -f "$DATA/done_$JOB.part" "$DATA/done_$JOB.tsv"
    exit 0
}

# fresh <file> <minutes>: true when the file exists and is newer than that
fresh() {
    [ -n "$(find "$1" -mmin "-$2" 2>/dev/null)" ]
}

# The proxy curl uses, without any password in it
proxy() {
    printf '%s' "${https_proxy:-${HTTPS_PROXY:-${all_proxy:-$ALL_PROXY}}}" \
        | sed 's#//[^@/]*@#//#'
}

# note <reason> <host> [detail]: remember why GitHub couldn't be used. The first one counts
note() {
    [ -f "$WHY" ] && return
    printf '%s\t%s\t%s\n' "$1" "$2" "$(printf '%s' "$3" | tr '\t{}\\' '  ()/' | cut -c 1-120)" \
        > "$WHY"
}

# explain <curl exit code> <http code> <url> <file>: turn a failed curl into a reason
explain() {
    host=$(printf '%s' "$3" | sed 's#^[a-z]*://##; s#/.*##')
    err=$(tr -d '\r' < "$4.err" 2>/dev/null | head -n 1 | sed 's/^curl: ([0-9]*) //')
    case "$1" in
        0)
            case "$2" in
                200) note notgithub "$host" ;;
                403|429)
                    if grep -qi '^x-ratelimit-remaining: *0' "$4.head" 2>/dev/null; then
                        reset=$(grep -i '^x-ratelimit-reset:' "$4.head" | tr -cd '0-9')
                        printf '%s\n' "$reset" > "$DATA/limited"
                        note limit "$host" "$reset"
                    else
                        note denied "$host" "$2"
                    fi ;;
                404) note missing "$host" "$2" ;;
                5??) note githubdown "$host" "$2" ;;
                *) note http "$host" "$2" ;;
            esac ;;
        5|97) note proxy "$host" "$(proxy)" ;;
        6) note dns "$host" ;;
        7)
            case "$err" in
                *nreachable*|*"No route"*) note unreachable "$host" ;;
                *)
                    if [ -n "$(proxy)" ]; then
                        note proxy "$host" "$(proxy)"
                    else
                        note refused "$host"
                    fi ;;
            esac ;;
        28)
            case "$err" in
                Resolving*|*"resolve"*) note dns "$host" ;;
                *onnect*)
                    if [ -n "$(proxy)" ]; then
                        note proxy "$host" "$(proxy)"
                    else
                        note timeout "$host"
                    fi ;;
                *) note slow "$host" ;;
            esac ;;
        35|51|53|54|58|59|60|64|66|77|80|82|83|90|91)
            if [ "$(date +%Y)" -lt 2025 ]; then
                note clock "$host" "$(date '+%Y-%m-%d')"
            else
                note tls "$host" "$err"
            fi ;;
        16|18|52|55|56|92) note cutoff "$host" ;;
        *) note other "$host" "$err" ;;
    esac
}

# fetch <url> <file> [json]: save the answer to <file> only when it's 200 OK. With json, it
# also has to be JSON, since a network that shows its own login page (hotel or work Wi-Fi)
# answers 200 with a web page
fetch() {
    rm -f "$2.part" "$2.head" "$2.err"
    code=$(curl -sS -L --connect-timeout 10 --max-time 25 \
        -H "Accept: application/vnd.github+json" -H "User-Agent: 3kdb-dblog" \
        -D "$2.head" -o "$2.part" -w '%{http_code}' "$1" 2>"$2.err")
    result=$?
    ok=0
    if [ "$result" = 0 ] && [ "$code" = 200 ]; then
        ok=1
        first=$(head -c 200 "$2.part" | tr -d ' \t\r\n' | cut -c 1)
        if [ "$3" = "json" ] && [ "$first" != "[" ] && [ "$first" != "{" ]; then
            ok=0
        elif [ "$3" = "feed" ] && ! grep -q '<feed' "$2.part"; then
            ok=0
        fi
    fi
    if [ "$ok" = 1 ]; then
        mv -f "$2.part" "$2"
    else
        explain "$result" "$code" "$1" "$2"
        rm -f "$2.part"
    fi
    rm -f "$2.head" "$2.err"
    [ "$ok" = 1 ]
}

# api_ok: GitHub's API can be asked. Not once it failed this run, and not while the hourly
# limit is used up, so a blocked connection is only waited for once
api_ok() {
    command -v curl > /dev/null 2>&1 || return 1
    [ -f "$WHY" ] && return 1
    reset=$(cat "$DATA/limited" 2>/dev/null | tr -cd '0-9')
    if [ -n "$reset" ] && [ "$reset" -gt "$(date +%s)" ]; then
        note limit api.github.com "$reset"
        return 1
    fi
    return 0
}

# Every JSON string GitHub sends is read by jstr: it decodes escapes and makes the text safe
# to print in tt++ (no braces, backslashes, tabs or colour codes)
AWK_LIB='
function jstr(s, i,    out, c, n, cp, lo) {
    out = ""
    n = length(s)
    while (i <= n) {
        c = substr(s, i, 1)
        if (c == "\"") {
            break
        }
        if (c == "\\") {
            i++
            c = substr(s, i, 1)
            if (c == "n") {
                c = "\n"
            } else if (c == "t" || c == "r") {
                c = " "
            } else if (c == "u") {
                cp = hexval(substr(s, i + 1, 4))
                i += 4
                if (cp >= 55296 && cp <= 56319 && substr(s, i + 1, 2) == "\\u") {
                    lo = hexval(substr(s, i + 3, 4))
                    i += 6
                    cp = 65536 + (cp - 55296) * 1024 + (lo - 56320)
                }
                c = utf8(cp)
            }
        }
        out = out c
        i++
    }
    JEND = i
    return out
}
# A \u escape as the UTF-8 bytes of that character, with emoji sent as two halves joined
function utf8(cp) {
    if (cp < 32) {
        return " "
    }
    if (cp < 128) {
        return sprintf("%c", cp)
    }
    if (cp < 2048) {
        return sprintf("%c%c", 192 + int(cp / 64), 128 + cp % 64)
    }
    if (cp < 65536) {
        return sprintf("%c%c%c", 224 + int(cp / 4096), 128 + int(cp / 64) % 64, 128 + cp % 64)
    }
    return sprintf("%c%c%c%c", 240 + int(cp / 262144), 128 + int(cp / 4096) % 64,
        128 + int(cp / 64) % 64, 128 + cp % 64)
}
function hexval(h,    v, k) {
    v = 0
    for (k = 1; k <= length(h); k++) {
        v = v * 16 + index("0123456789abcdef", tolower(substr(h, k, 1))) - 1
    }
    return v
}
function safe(t,    out) {
    gsub(/\t/, " ", t)
    gsub(/\{/, "(", t)
    gsub(/\}/, ")", t)
    gsub(/\\/, "/", t)
    out = ""
    while (match(t, /<[0-9A-Za-z][0-9A-Za-z][0-9A-Za-z]>/)) {
        out = out substr(t, 1, RSTART - 1) "(" substr(t, RSTART + 1, 3) ")"
        t = substr(t, RSTART + RLENGTH)
    }
    return out t
}
# GitHub sends no spaces between the parts of its JSON, but these allow any spacing anyway.
# A key cannot match inside a string value, where its quotes would have a backslash before them.
function key_re(key) {
    return "\"" key "\"[ \t\r]*:[ \t\r]*"
}
function commit_re() {
    return "[{][ \t\r]*" key_re("sha") "\"[0-9a-f]+\"[ \t\r]*,[ \t\r]*" key_re("node_id") "\"C_"
}
function value_after(s, key) {
    if (!match(s, key_re(key) "\"")) {
        return ""
    }
    return jstr(s, RSTART + RLENGTH)
}
function sha_of(s) {
    if (!match(s, key_re("sha") "\"")) {
        return ""
    }
    return substr(s, RSTART + RLENGTH, 40)
}
# add_commit and print_rows turn commits from any source into history rows, newest first.
# Merges, branch syncs and reverted pairs are left out, and the body loses its sign-off lines.
function add_commit(sha, date, author, msg, parents,
    lines, subject, body, kept, blank, k, line, low) {
    if (sha == "" || parents > 1) {
        return
    }
    split(msg, lines, "\n")
    subject = lines[1]
    if (subject ~ /^Merge (branch|remote-tracking branch|pull request) /) {
        return
    }
    if (match(msg, /This reverts commit [0-9a-f]+/)) {
        GONE[substr(msg, RSTART + 20, RLENGTH - 20)] = 1
        GONE[sha] = 1
    }
    body = ""
    kept = 0
    blank = 0
    for (k = 2; k in lines; k++) {
        line = lines[k]
        sub(/[ \t]+$/, "", line)
        low = tolower(line)
        sub(/^[ \t]+/, "", low)
        if (low ~ /^(co-authored-by|signed-off-by|reviewed-by|\(cherry picked from)/) {
            continue
        }
        if (index(line, "chars/")) {
            continue
        }
        if (line == "") {
            blank = kept
            continue
        }
        if (blank && kept) {
            body = body "{" (++kept) "}{}"
        }
        blank = 0
        body = body "{" (++kept) "}{" safe(line) "}"
    }
    ROWS++
    ROW_SHA[ROWS] = sha
    ROW_TEXT[ROWS] = date "\t" safe(author) "\t" safe(subject) "\t" body
}
function print_rows(    r, sha, hidden, g) {
    for (r = 1; r <= ROWS; r++) {
        sha = ROW_SHA[r]
        hidden = (sha in GONE)
        for (g in GONE) {
            if (length(g) < 40 && index(sha, g) == 1) {
                hidden = 1
            }
        }
        if (!hidden) {
            print sha "\t" ROW_TEXT[r]
        }
    }
}
'

# history_rows <page files...>: the API's commit lists as history rows
history_rows() {
    awk "$AWK_LIB"'
    { text = text $0 }
    END {
        gsub(commit_re(), "\n&", text)
        count = split(text, rec, "\n")
        for (r = 2; r <= count; r++) {
            s = rec[r]
            if (!match(s, key_re("commit") "[{][ \t\r]*" key_re("author") "[{]")) {
                continue
            }
            s2 = substr(s, RSTART)
            parents = 0
            if (match(s, key_re("parents") "\\[")) {
                tail = substr(s, RSTART)
                parents = gsub(key_re("sha") "\"", "&", tail)
            }
            add_commit(sha_of(s), substr(value_after(s2, "date"), 1, 10),
                value_after(s2, "name"), value_after(s2, "message"), parents)
        }
        print_rows()
    }' "$@"
}

# feed_rows <feed file>: github.com's feed of the newest 20 changes as history rows. The
# write-up is HTML inside XML, so it's unescaped twice and its tags are dropped
feed_rows() {
    awk "$AWK_LIB"'
    function unxml(t) {
        gsub(/&lt;/, "<", t)
        gsub(/&gt;/, ">", t)
        gsub(/&quot;/, "\"", t)
        gsub(/&#39;/, "\047", t)
        gsub(/&amp;/, "\\&", t)
        return t
    }
    /<entry>/ {
        inside = 1
        sha = ""
        date = ""
        author = ""
        msg = ""
        content = 0
        next
    }
    inside && /<\/entry>/ {
        msg = unxml(msg)
        gsub(/<[^>]*>/, "", msg)
        msg = unxml(msg)
        sub(/^[ \t\n]+/, "", msg)
        sub(/[ \t\n]+$/, "", msg)
        add_commit(sha, date, author, msg, 1)
        inside = 0
        next
    }
    !inside {
        next
    }
    content {
        line = $0
        if (sub(/<\/content>.*/, "", line)) {
            content = 0
        }
        msg = msg "\n" line
        next
    }
    /<content/ {
        line = $0
        sub(/.*<content[^>]*>/, "", line)
        if (sub(/<\/content>.*/, "", line) == 0) {
            content = 1
        }
        msg = line
        next
    }
    /<id>/ && match($0, /Commit\/[0-9a-f]+/) {
        sha = substr($0, RSTART + 7, RLENGTH - 7)
    }
    /<updated>/ && date == "" && match($0, /[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/) {
        date = substr($0, RSTART, 10)
    }
    /<name>/ && author == "" {
        author = $0
        sub(/.*<name>/, "", author)
        sub(/<\/name>.*/, "", author)
        author = unxml(author)
    }
    END {
        print_rows()
    }' "$1"
}

# local_rows <ref>: this folder's own git history as history rows. Each change's files go in
# files/, as GitHub would list them. Nothing here uses the network
local_rows() {
    GIT_TERMINAL_PROMPT=0 git -c safe.directory="$(pwd)" log -n 300 --date=short \
        --name-only --no-renames --format='%x1e%H%x1f%ad%x1f%an%x1f%P%x1f%B%x1d' "$1" \
        2>/dev/null | awk -v files_dir="$DATA/files" "$AWK_LIB"'
    BEGIN {
        RS = "\036"
    }
    NR > 1 {
        end = index($0, "\035")
        split(substr($0, 1, end - 1), f, "\037")
        listed = substr($0, end + 1)
        n = split(listed, names, "\n")
        out = files_dir "/" f[1]
        printf "" > out
        for (k = 1; k <= n; k++) {
            if (names[k] != "") {
                print safe(names[k]) > out
            }
        }
        close(out)
        add_commit(f[1], f[2], f[3], f[5], split(f[4], p, " "))
    }
    END {
        print_rows()
    }'
}

# shas_in <json>: the commit hashes in a commit list answer
shas_in() {
    awk "$AWK_LIB"'
    { text = text $0 }
    END {
        while (match(text, commit_re())) {
            found = substr(text, RSTART, RLENGTH)
            text = substr(text, RSTART + RLENGTH)
            print sha_of(found)
        }
    }' "$1"
}

# names_in <json> <key>: every string value of that key, one per line
names_in() {
    awk "$AWK_LIB"'
    { text = text $0 }
    END {
        while (match(text, key_re(KEY) "\"")) {
            text = substr(text, RSTART + RLENGTH)
            print safe(jstr(text, 1))
            text = substr(text, JEND)
        }
    }' KEY="$2" "$1"
}

# Ask GitHub's API for the latest 300 master commits. history.tsv is only replaced when every
# page came back as commits
refresh_history() {
    api_ok || return 1
    for page in $PAGES; do
        fetch "$API/commits?sha=master&per_page=100&page=$page" \
            "$DATA/page${page}_$JOB.json" json &
    done
    wait
    got=1
    for page in $PAGES; do
        [ -f "$DATA/page${page}_$JOB.json" ] || got=0
    done
    if [ "$got" = 1 ]; then
        history_rows "$DATA"/page1_"$JOB".json "$DATA"/page2_"$JOB".json \
            "$DATA"/page3_"$JOB".json > "$DATA/history_$JOB.part"
        if [ -s "$DATA/history_$JOB.part" ]; then
            mv -f "$DATA/history_$JOB.part" "$DATA/history.tsv"
        else
            note notgithub api.github.com
            got=0
        fi
    fi
    rm -f "$DATA"/page*_"$JOB".json "$DATA/history_$JOB.part"
    [ "$got" = 1 ]
}

# Top up the saved list with github.com's feed, or start one from it. A saved list is only
# changed when the feed reaches back to its newest change, so there's never a gap
use_feed() {
    command -v curl > /dev/null 2>&1 || return 1
    fetch "$FEED" "$DATA/feed_$JOB.xml" feed || return 1
    feed_rows "$DATA/feed_$JOB.xml" > "$DATA/feedrows_$JOB.tsv"
    rm -f "$DATA/feed_$JOB.xml"
    if [ ! -s "$DATA/feedrows_$JOB.tsv" ]; then
        rm -f "$DATA/feedrows_$JOB.tsv"
        return 1
    fi
    if [ -s "$DATA/history.tsv" ]; then
        newest=$(head -n 1 "$DATA/history.tsv" | cut -f 1)
        if cut -f 1 "$DATA/feedrows_$JOB.tsv" | grep -q "^$newest\$"; then
            {
                awk -F '\t' -v stop="$newest" '$1 == stop { exit } { print }' \
                    "$DATA/feedrows_$JOB.tsv"
                cat "$DATA/history.tsv"
            } > "$DATA/history_$JOB.part"
            mv -f "$DATA/history_$JOB.part" "$DATA/history.tsv"
            SOURCE="feed"
        fi
        rm -f "$DATA/feedrows_$JOB.tsv"
        [ "$SOURCE" = "feed" ]
        return
    fi
    mv -f "$DATA/feedrows_$JOB.tsv" "$DATA/history.tsv"
    SOURCE="feed"
}

# The ref that holds GitHub's master in this clone, else this checkout
local_ref() {
    for ref in upstream/master origin/master; do
        if git -c safe.directory="$(pwd)" rev-parse --verify --quiet "$ref" > /dev/null 2>&1
        then
            printf '%s' "$ref"
            return
        fi
    done
    printf 'HEAD'
}

# This folder's own git history, when GitHub can't be reached and nothing is saved
use_local() {
    command -v git > /dev/null 2>&1 || return 1
    git -c safe.directory="$(pwd)" rev-parse --git-dir > /dev/null 2>&1 || return 1
    local_rows "$(local_ref)" > "$DATA/local_$JOB.tsv"
    if [ -s "$DATA/local_$JOB.tsv" ]; then
        mv -f "$DATA/local_$JOB.tsv" "$DATA/local.tsv"
        SOURCE="local"
        return 0
    fi
    rm -f "$DATA/local_$JOB.tsv"
    return 1
}

# get_files <sha...>: ask GitHub which files each change touched, and keep the answer for good
get_files() {
    api_ok || return
    for sha in "$@"; do
        (
            if fetch "$API/commits/$sha" "$DATA/files/$sha.json" json; then
                names_in "$DATA/files/$sha.json" filename > "$DATA/files/$sha.part"
                mv -f "$DATA/files/$sha.part" "$DATA/files/$sha"
            fi
            rm -f "$DATA/files/$sha.json"
        ) &
    done
    wait
}

# The newest FILE_TOP changes that have no file list yet, up to FILE_FETCHES of them. That's
# enough to hide the character-only ones from the first pages, and keeps under GitHub's limit
missing_files() {
    head -n "$FILE_TOP" "$HISTORY" | cut -f 1 | while read -r sha; do
        [ -f "$DATA/files/$sha" ] || echo "$sha"
    done | head -n "$FILE_FETCHES"
}

# commits.tsv: the history with each change's files joined on, as a|b|c, or ? when not known.
# chars/, vars/ and logs/ don't count, and a change that only touched those is left out.
build_commits() {
    {
        printf 'sha\tdate\tauthor\tsubject\tbody\tfiles\n'
        cut -f 1 "$HISTORY" | while read -r sha; do
            if [ -f "$DATA/files/$sha" ]; then
                printf '%s\t' "$sha"
                tr '\n' '|' < "$DATA/files/$sha"
                printf '\n'
            fi
        done > "$DATA/known_$JOB.tsv"
        awk -F '\t' -v known_file="$DATA/known_$JOB.tsv" '
        FILENAME == known_file {
            n = split($2, all, "|")
            list = ""
            seen = 0
            for (k = 1; k <= n; k++) {
                if (all[k] == "") {
                    continue
                }
                seen++
                if (all[k] !~ /^(chars|vars|logs)\//) {
                    list = list (list == "" ? "" : "|") all[k]
                }
            }
            files[$1] = list
            known[$1] = seen
            next
        }
        {
            if (($1 in known) && known[$1] > 0 && files[$1] == "") {
                next
            }
            body = $5
            gsub(/\{[0-9]+\}/, " ", body)
            gsub(/[{}]/, " ", body)
            gsub(/  +/, " ", body)
            sub(/^ /, "", body)
            sub(/ $/, "", body)
            print $1 "\t" $2 "\t" $3 "\t" $4 "\t" body "\t" (($1 in known) ? files[$1] : "?")
        }' "$DATA/known_$JOB.tsv" "$HISTORY"
    } > "$DATA/commits_$JOB.part"
    rm -f "$DATA/known_$JOB.tsv"
    mv -f "$DATA/commits_$JOB.part" "$DATA/commits.tsv"
}

# show_<job>.tsv for show <hash>: the change's hash, then its write-up and files, one per line
write_show() {
    hex=$(printf '%s' "$1" | tr -cd '0-9a-fA-F' | tr 'A-F' 'a-f')
    {
        printf 'kind\ttext\n'
        [ "${#hex}" -ge 4 ] && awk -F '\t' -v hex="$hex" '
        FNR > 1 && index($1, hex) == 1 {
            print "sha\t" $1
            sha = $1
            files = $6
            exit
        }
        END {
            if (sha == "") {
                exit
            }
            while ((getline line < HISTORY) > 0) {
                split(line, f, "\t")
                if (f[1] != sha) {
                    continue
                }
                body = f[5]
                while (match(body, /^\{[0-9]+\}\{[^}]*\}/)) {
                    part = substr(body, 1, RLENGTH)
                    sub(/^\{[0-9]+\}\{/, "", part)
                    print "body\t" substr(part, 1, length(part) - 1)
                    body = substr(body, RLENGTH + 1)
                }
                break
            }
            if (files == "?") {
                print "nofiles\t"
            } else {
                n = split(files, all, "|")
                for (k = 1; k <= n; k++) {
                    if (all[k] != "") {
                        print "file\t" all[k]
                    }
                }
            }
        }' HISTORY="$HISTORY" "$DATA/commits.tsv"
    } > "$DATA/show_$JOB.part"
    mv -f "$DATA/show_$JOB.part" "$DATA/show_$JOB.tsv"
}

# head_<job>.tsv: the commits this checkout has, read from local git (no network)
write_head() {
    command -v git > /dev/null 2>&1 || return
    git -c safe.directory="$(pwd)" rev-parse --git-dir > /dev/null 2>&1 || return
    {
        printf 'sha\n'
        GIT_TERMINAL_PROMPT=0 git -c safe.directory="$(pwd)" rev-list --max-count=3000 HEAD \
            2>/dev/null
    } > "$DATA/head_$JOB.part"
    mv -f "$DATA/head_$JOB.part" "$DATA/head_$JOB.tsv"
}

# diff_<job>.tsv for new, when this folder isn't a git clone (or git isn't installed): GitHub's
# current files are downloaded from github.com and compared with this folder's, one by one.
# chars/, vars/ and logs/ are left out, and Windows line endings count as the same file
write_diff() {
    mkdir -p "$DATA/github_$JOB"
    got=0
    if fetch "$TARBALL" "$DATA/github_$JOB.tgz"; then
        if tar -xzf "$DATA/github_$JOB.tgz" -C "$DATA/github_$JOB" 2>/dev/null; then
            got=1
        else
            note notgithub github.com
        fi
    fi
    if [ "$got" = 0 ]; then
        rm -rf "$DATA/github_$JOB" "$DATA/github_$JOB.tgz"
        printf 'kind\tpath\nfailed\t\n' > "$DATA/diff_$JOB.part"
        mv -f "$DATA/diff_$JOB.part" "$DATA/diff_$JOB.tsv"
        return
    fi
    rm -f "$DATA/github_$JOB.tgz"
    top=$(ls "$DATA/github_$JOB" | head -n 1)
    printf 'kind\tpath\n' > "$DATA/diff_$JOB.part"
    (cd "$DATA/github_$JOB/$top" && find . -type f | sed 's#^\./##' | sort) \
        | grep -v -E '^(chars|vars|logs)/' > "$DATA/list_$JOB.txt"
    while read -r path; do
        theirs="$DATA/github_$JOB/$top/$path"
        if [ ! -f "$path" ]; then
            printf 'missing\t%s\n' "$path"
        elif ! cmp -s "$theirs" "$path"; then
            tr -d '\r' < "$theirs" > "$DATA/a_$JOB.tmp"
            tr -d '\r' < "$path" > "$DATA/b_$JOB.tmp"
            cmp -s "$DATA/a_$JOB.tmp" "$DATA/b_$JOB.tmp" || printf 'changed\t%s\n' "$path"
        fi
    done < "$DATA/list_$JOB.txt" | tr '{}\\' '()/' >> "$DATA/diff_$JOB.part"
    printf 'total\t%s\n' "$(wc -l < "$DATA/list_$JOB.txt" | tr -d ' ')" >> "$DATA/diff_$JOB.part"
    rm -rf "$DATA/github_$JOB" "$DATA/list_$JOB.txt" "$DATA/a_$JOB.tmp" "$DATA/b_$JOB.tmp"
    mv -f "$DATA/diff_$JOB.part" "$DATA/diff_$JOB.tsv"
}

# match_<job>.tsv for file <part>...: GitHub lists the changes to each matching file or folder.
# Folders are asked once (file map asks for common/map, not each map file), up to 8 asks.
write_matches() {
    if ! fresh "$DATA/tree.txt" 60 && api_ok; then
        if fetch "$API/git/trees/master?recursive=1" "$DATA/tree_$JOB.json" json; then
            names_in "$DATA/tree_$JOB.json" path > "$DATA/tree_$JOB.part"
            mv -f "$DATA/tree_$JOB.part" "$DATA/tree.txt"
        fi
        rm -f "$DATA/tree_$JOB.json"
    fi
    printf 'part\tsha\n' > "$DATA/match_$JOB.part"
    for part in "$@"; do
        awk -v part="$part" '
        $0 !~ /^(chars|vars|logs)\// && index(tolower($0), part) {
            n = split($0, bits, "/")
            path = ""
            for (k = 1; k <= n; k++) {
                path = path (k > 1 ? "/" : "") bits[k]
                if (index(tolower(path), part)) {
                    break
                }
            }
            if (!(path in done)) {
                done[path] = 1
                print path
            }
        }' "$DATA/tree.txt" 2>/dev/null | head -n 9 > "$DATA/paths_$JOB.txt"
        if [ "$(wc -l < "$DATA/paths_$JOB.txt")" -gt 8 ]; then
            printf '%s\ttoo many\n' "$part" >> "$DATA/match_$JOB.part"
        elif api_ok; then
            num=0
            while read -r path; do
                num=$((num + 1))
                path=$(printf '%s' "$path" | sed -e 's/%/%25/g' -e 's/ /%20/g' -e 's/#/%23/g' \
                    -e 's/&/%26/g' -e 's/+/%2B/g')
                fetch "$API/commits?sha=master&per_page=100&path=$path" \
                    "$DATA/path${num}_$JOB.json" json &
            done < "$DATA/paths_$JOB.txt"
            wait
            for json in "$DATA"/path*_"$JOB".json; do
                [ -f "$json" ] && shas_in "$json" | awk -v part="$part" '{ print part "\t" $0 }'
            done >> "$DATA/match_$JOB.part"
            rm -f "$DATA"/path*_"$JOB".json
        fi
        # Changes whose file lists are already known count too, even for deleted files
        for known in "$DATA"/files/*; do
            [ -f "$known" ] || continue
            grep -v -E '^(chars|vars|logs)/' "$known" | grep -q -i -F -- "$part" \
                && printf '%s\t%s\n' "$part" "${known##*/}"
        done >> "$DATA/match_$JOB.part"
        rm -f "$DATA/paths_$JOB.txt"
    done
    mv -f "$DATA/match_$JOB.part" "$DATA/match_$JOB.tsv"
}

if ! command -v curl > /dev/null 2>&1; then
    note nocurl ""
fi

# Only one dblog asks GitHub at a time. The others wait for it, then use what it got
lock="$DATA/lock"
waited=0
while ! mkdir "$lock" 2>/dev/null; do
    if [ -n "$(find "$lock" -mmin +2 2>/dev/null)" ] || [ "$waited" -ge 80 ]; then
        rmdir "$lock" 2>/dev/null
        continue
    fi
    sleep 1
    waited=$((waited + 1))
done
trap 'rmdir "$lock" 2>/dev/null' EXIT

# A list from the API that's new enough is used as it is. Otherwise ask again, and when that
# fails, fall back to the saved list, the feed, then this folder's git history
if [ "$MODE" = "new" ]; then
    max_age=1
elif [ "$waited" -gt 0 ] && [ -s "$DATA/history.tsv" ]; then
    max_age=100000
else
    max_age=10
fi
if ! fresh "$DATA/history.tsv" "$max_age" || [ ! -s "$DATA/history.tsv" ]; then
    if ! refresh_history; then
        use_feed || SOURCE="saved"
        if [ ! -s "$DATA/history.tsv" ]; then
            use_local || SOURCE="none"
        fi
    fi
fi

HISTORY="$DATA/history.tsv"
if [ "$SOURCE" = "local" ]; then
    HISTORY="$DATA/local.tsv"
fi
if [ "$SOURCE" = "none" ]; then
    printf 'sha\tdate\tauthor\tsubject\tbody\tfiles\n' > "$DATA/commits.tsv"
    finish
fi

if [ "$SOURCE" != "local" ]; then
    # shellcheck disable=SC2046
    get_files $(missing_files)
    hex=$(printf '%s' "$1" | tr -cd '0-9a-fA-F' | tr 'A-F' 'a-f')
    if [ "$MODE" = "show" ] && [ "${#hex}" -ge 4 ]; then
        sha=$(cut -f 1 "$HISTORY" | grep -m 1 "^$hex")
        if [ -n "$sha" ] && [ ! -f "$DATA/files/$sha" ]; then
            get_files "$sha"
        fi
    fi
fi
build_commits
rmdir "$lock" 2>/dev/null

case "$MODE" in
    new)
        write_head
        [ -f "$DATA/head_$JOB.tsv" ] || write_diff ;;
    list) write_head ;;
    file) write_matches "$@" ;;
    show) write_show "$1" ;;
esac
finish
