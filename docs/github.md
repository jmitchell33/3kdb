# 3kdb Git and GitHub Guide

This guide covers updating 3kdb, keeping your own changes, and sending changes to the project. If you haven't installed 3kdb yet, start with **[setup.md](setup.md)**. For everything else, see the [manual](manual.md) and [FAQ](faq.md).

Anything in a grey box is something to type or paste. **Paste with a right-click or `Ctrl+Shift+V`**, because plain `Ctrl+V` usually doesn't work in a terminal.

`3kdb` is the default folder name. If you renamed yours, use your folder's name wherever you see `~/3kdb`. `byron` is an example, so use your own character's name.

## Contents

- [Part 1: Which one do I need?](#part-1-which-one-do-i-need)
- [Part 2: Just cloned, no GitHub account](#part-2-just-cloned-no-github-account)
  - [Get updates](#get-updates)
  - [Keep your changes and still update](#keep-your-changes-and-still-update)
- [Part 3: Set up a fork from scratch](#part-3-set-up-a-fork-from-scratch)
- [Part 4: Switch an existing clone to a fork](#part-4-switch-an-existing-clone-to-a-fork)
- [Part 5: Install the git helpers](#part-5-install-the-git-helpers)
- [Part 6: Everyday routine](#part-6-everyday-routine)
- [Part 7: What each helper does](#part-7-what-each-helper-does)
- [Part 8: Open pull requests](#part-8-open-pull-requests)
- [Part 9: Merge conflicts](#part-9-merge-conflicts)
- [Part 10: Playing while using git](#part-10-playing-while-using-git)
- [Part 11: Problems and fixes](#part-11-problems-and-fixes)

---

## Part 1: Which one do I need?

- **Only want to play and get updates?** You just need a clone. Go to [Part 2](#part-2-just-cloned-no-github-account).
- **Want to send changes to the project?** You need a fork. Go to [Part 3](#part-3-set-up-a-fork-from-scratch).
- **Already cloned, and now want a fork?** Go to [Part 4](#part-4-switch-an-existing-clone-to-a-fork).

**The three places your code can live:**

- `upstream` is `jmitchell33/3kdb`, the main project. Pull requests get merged here.
- `origin` is your fork on GitHub. With a plain clone, `origin` is the main project instead, and you can't send changes to it.
- `local` is the copy on your computer.

[Back to top](#3kdb-git-and-github-guide)

---

## Part 2: Just cloned, no GitHub account

### Get updates

```bash
cd ~/3kdb
git pull
```

If you're logged in, log out and back in to load the new code.

### Keep your changes and still update

If you edited files that the project also changed, `git pull` stops with this message:

```text
error: Your local changes to the following files would be overwritten by merge
```

Nothing is lost when that happens. **The helper commands don't handle this for a plain clone**, because they need a fork. Use these steps instead. They save your changes in git, then merge the update in.

**1. Tell git who you are.** You only do this once. Any name and email will work.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**2. Save your changes.** If it says `nothing to commit`, that's fine, so carry on.

```bash
cd ~/3kdb
git add .
git reset -q -- '*vars.tin'
git commit -m "my changes"
```

**3. Get the update.** Once you've saved changes this way, always use this command to update instead of plain `git pull`:

```bash
git pull --no-rebase --no-edit
```

There are three possible results:

- **It finishes with no complaint.** You're done. You have your changes and the update.
- **It says `CONFLICT`.** You and the project changed the same lines. Follow [Part 9](#part-9-merge-conflicts), using the steps for a plain clone.
- **It complains about a `vars.tin` file.** Do step 4.

**4. Only if a `vars.tin` file blocked the update.** The game keeps rewriting this file. This moves your copy aside, updates, then puts it back:

```bash
cp chars/byron/vars.tin ~/my-vars.tin
git checkout -- chars/byron/vars.tin
git pull --no-rebase --no-edit
cp ~/my-vars.tin chars/byron/vars.tin
```

[Back to top](#3kdb-git-and-github-guide)

---

## Part 3: Set up a fork from scratch

Do this if you haven't downloaded 3kdb yet. You only do it once. If you've already downloaded it, use [Part 4](#part-4-switch-an-existing-clone-to-a-fork) instead.

**1. Make a GitHub account** at https://github.com/signup. Remember your username, and verify your email address.

**2. Windows only:** install Ubuntu as shown in [setup.md Step 1](setup.md#step-1-install-tintin-and-git), and do the rest in the Ubuntu window.

**3. Install git and the GitHub tool (`gh`):**

```bash
sudo apt update
sudo apt install -y git gh
```

If it says `gh` can't be found, follow the Linux steps at https://cli.github.com instead. On a Mac, install Homebrew from https://brew.sh, then run:

```bash
brew install git gh
```

**4. Tell git who you are.** Use your own name and GitHub email, and keep the quotes.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**5. Turn on a setting the helpers need:**

```bash
git config --global push.autoSetupRemote true
```

**6. Log in to GitHub:**

```bash
gh auth login
```

Pick **GitHub.com**, **HTTPS**, **Yes** (authenticate Git), and **Login with a web browser**. It shows a code. Copy it and press Enter. If no browser opens, go to https://github.com/login/device and enter the code there.

**7. Make your fork and download it:**

```bash
cd ~
gh repo fork jmitchell33/3kdb --clone
cd 3kdb
```

**8. Check it worked:**

```bash
git remote -v
```

You should see two names:

```text
origin    https://github.com/YOUR-USERNAME/3kdb.git
upstream  https://github.com/jmitchell33/3kdb.git
```

If `upstream` is missing, add it:

```bash
git remote add upstream https://github.com/jmitchell33/3kdb.git
```

**9. Install the helpers** with [Part 5](#part-5-install-the-git-helpers), then carry on with [setup.md Step 3](setup.md#step-3-open-the-menu).

[Back to top](#3kdb-git-and-github-guide)

---

## Part 4: Switch an existing clone to a fork

Do this if you cloned `jmitchell33/3kdb` and now want to send changes. Your characters and edits stay where they are, and you don't need to download anything again.

**1. Do steps 1 to 6 of [Part 3](#part-3-set-up-a-fork-from-scratch).** That covers the account, tools and login. Then come back here.

**2. Make your fork and link your folder to it:**

```bash
cd ~/3kdb
gh repo fork --remote
```

This renames your old `origin` to `upstream`, and makes your new fork the `origin`.

**3. Check it worked:**

```bash
git remote -v
```

You should see:

```text
origin    https://github.com/YOUR-USERNAME/3kdb.git
upstream  https://github.com/jmitchell33/3kdb.git
```

**4. Install the helpers** with [Part 5](#part-5-install-the-git-helpers).

**5. If you've changed any files,** move those changes onto their own branch. `master` should only ever hold what the main project has. If you never changed anything, skip to step 6.

Do you want to keep your character's folder off GitHub? Forks are public, and the next commands upload new files. `private.tin` is always left out, and so is `vars.tin` for a new character, but the rest of `chars/byron/` would go up. To keep the whole folder private, run this first:

```bash
echo 'chars/byron/' >> .git/info/exclude
```

Now move your changes. This works whether or not you've already committed them:

```bash
git checkout -b my-changes
git-save "my changes"
```

Then point `master` back at the main project. This doesn't touch your files, and your changes are safe on `my-changes`:

```bash
git fetch upstream
git branch -f master upstream/master
```

**6. Bring everything up to date:**

```bash
git-sync
```

If it says `MERGE CONFLICT`, see [Part 9](#part-9-merge-conflicts). This is how you keep your changes and the project's changes at the same time.

[Back to top](#3kdb-git-and-github-guide)

---

## Part 5: Install the git helpers

The helpers are short commands like `git-start` and `git-sync`. They go in your `.bashrc`, a settings file that loads each time you open a terminal.

**You also use this to update.** Paste the same block again when the helpers change, such as to get the newest `git-save`. It replaces the old block instead of adding a second copy. If you installed an older copy by hand, it can stay where it is, because this one loads after it and takes over.

**1. Copy the whole box below.** It's long, so use the copy button if you see one. You can run it from any folder.

```bash
sed -i.bak '/^# >>> 3kdb git helpers >>>$/,/^# <<< 3kdb git helpers <<<$/d' ~/.bashrc
cat >> ~/.bashrc <<'EOF'
# >>> 3kdb git helpers >>>
# git-save [message]: stage everything, commit (default "savepoint") if anything
# changed, then push -- also pushes commits already made.
# Refuses to run on master, which should only ever hold what upstream has.
unalias git-save 2>/dev/null
git-save() {
  if [ "$(git branch --show-current)" = "master" ]; then
    echo "git-save: you are on master. Make a branch first: git-start <name>"
    return 1
  fi
  git add . || return
  if git diff --cached --quiet; then
    echo "git-save: nothing new to commit"
  else
    git commit -m "${*:-savepoint}" || return
  fi
  git push
}

# git-keep-vars <command...>: run a git command with changed vars.tin files moved out of the way,
# then put them back. Example: git-keep-vars git checkout sandbox9
# A running game keeps rewriting chars/<you>/vars.tin, and that would otherwise
# stop git from switching branches. If the game saves mid-command, it tries again.
git-keep-vars() {
  local top backup tries=1 result
  top=$(git rev-parse --show-toplevel) || return
  mkdir -p "$HOME/3kdb-temp" || return
  backup=$(mktemp -d "$HOME/3kdb-temp/vars-backup.XXXXXX") || return
  while :; do
    git -C "$top" diff --name-only HEAD -- '*vars.tin' | while IFS= read -r file; do
      [ -f "$top/$file" ] || continue
      mkdir -p "$backup/$(dirname "$file")"
      cp -p "$top/$file" "$backup/$file"
      git -C "$top" checkout -q HEAD -- "$file"
    done
    "$@"
    result=$?
    [ "$result" -eq 0 ] && break
    [ "$tries" -ge 5 ] && break
    [ -n "$(git -C "$top" diff --name-only HEAD -- '*vars.tin')" ] || break
    echo "git-keep-vars: the game saved vars.tin just then, trying again..."
    tries=$((tries + 1))
    sleep 1
  done
  if [ -n "$(ls -A "$backup")" ]; then
    if cp -Rp "$backup/." "$top/"; then
      echo "git-keep-vars: kept your vars.tin changes."
    else
      echo "git-keep-vars: could not put vars.tin back. Your copy is safe in $backup"
      return 1
    fi
  fi
  rm -rf "$backup"
  return "$result"
}

# git-start <name>: update master, push it to your fork, then make a new branch from it.
# Safe to run while a game is running. Make up your own name, e.g. git-start fix-bard
unalias git-start 2>/dev/null
git-start() {
  if [ -z "$1" ]; then
    echo "Error: Provide a branch name. Example: git-start fix-bug"
    return 1
  fi
  if git show-ref --verify --quiet "refs/heads/$1"; then
    echo "git-start: a branch named $1 already exists. Pick a new name."
    return 1
  fi
  if [ "$(git branch --show-current)" = "master" ]; then
    git-keep-vars git pull upstream master || return
  else
    git fetch upstream master:master || return
  fi
  git push origin master || return
  git-keep-vars git checkout -b "$1" master || return
  echo "git-start: now on $1. A running game keeps what it has loaded, but anything"
  echo "           it loads from now on (relog, #read) comes from this branch."
}

# 2. Commit, push your branch to origin, and target the upstream repo for the PR
# Usage: git-pr "my update message"
alias git-pr='_git_pr() { \
    if [ -z "$1" ]; then echo "Error: Provide a commit description."; return 1; fi; \
    CURRENT_BRANCH=$(git branch --show-current); \
    if [ "$CURRENT_BRANCH" = "master" ]; then \
        echo "Error: You are on master! Create a branch first using git-start."; return 1; \
    fi; \
    git add . && \
    git commit -m "$1" 2>/dev/null || echo "No new local uncommitted changes found, attempting push..."; \
    git push -u origin "$CURRENT_BRANCH" && \
    gh pr create --repo jmitchell33/3kdb --base master --head "$(gh api user --jq .login):$CURRENT_BRANCH" --title "$1" --body "Automated branch PR."; \
}; _git_pr'

# 3. Pull latest upstream master changes into your current branch
# Usage: Run this inside your feature branch if you hit a conflict
alias git-sync-conflict='_git_sync_conflict() { \
    CURRENT_BRANCH=$(git branch --show-current); \
    if [ "$CURRENT_BRANCH" = "master" ]; then \
        echo "Error: You are on master."; return 1; \
    fi; \
    git checkout master && \
    git pull upstream master && \
    git checkout "$CURRENT_BRANCH" && \
    git merge master; \
}; _git_sync_conflict'

# Usage: git-pr-pro "My Clean Pull Request Title"
alias git-pr-pro='_git_pr_pro() { \
    if [ -z "$1" ]; then echo "Error: Provide a PR Title in quotes."; return 1; fi; \
    CURRENT_BRANCH=$(git branch --show-current); \
    if [ "$CURRENT_BRANCH" = "master" ] || [ "$CURRENT_BRANCH" = "main" ]; then \
        echo "Error: You are on master! Switch to your feature branch first."; return 1; \
    fi; \
    RAW_FILE="$HOME/3kdb-temp/pr.md"; \
    if [ ! -f "$RAW_FILE" ]; then \
        echo "Error: Could not find PR description file at $RAW_FILE"; return 1; \
    fi; \
    git add . && \
    git commit -m "$1" 2>/dev/null || echo "No new local uncommitted changes found (or already synced), attempting push..."; \
    git push -u origin "$CURRENT_BRANCH" && \
    gh pr create --repo jmitchell33/3kdb --base master --head "$(gh api user --jq .login):$CURRENT_BRANCH" --title "$1" --body-file "$RAW_FILE"; \
}; _git_pr_pro'

# Usage: Just type 'git-make-desc', paste your text, press Enter, then Ctrl+D.
# NOTE: Saves to ~/3kdb-temp/pr.md whatever your repo folder is called.
# git-pr-pro reads the same path, so change both if you rename it.
git-make-desc() {
    mkdir -p "$HOME/3kdb-temp"
    echo "--- Paste your PR body text below. When done, press Ctrl+D on a new blank line to save ---"
    cat > "$HOME/3kdb-temp/pr.md"
}

alias git-work='git checkout -b'

# git-sync: bring everything up to date with upstream (jmitchell33/3kdb).
#   1. saves and pushes any uncommitted work on your branch
#   2. updates local master from upstream
#   3. pushes master to your fork (clears "X commits behind" on GitHub)
#   4. merges master into your branch and pushes it
# Stops without pushing the merge if there is a conflict.
unalias git-sync 2>/dev/null
git-sync() {
  local branch
  branch=$(git branch --show-current)
  if [ -z "$branch" ]; then
    echo "git-sync: not on a branch, nothing done."
    return 1
  fi
  if git rev-parse -q --verify MERGE_HEAD >/dev/null; then
    echo "git-sync: a merge is still in progress. Fix the files and run git-save,"
    echo "          or cancel it with: git merge --abort"
    return 1
  fi

  if [ "$branch" = "master" ]; then
    git pull --ff-only upstream master || return
  else
    git-save "sync-$(date +%Y%m%d-%H%M)" || return
    git fetch upstream master:master || return
  fi
  git push origin master || return
  [ "$branch" = "master" ] && { echo "git-sync: master is up to date."; return 0; }

  if ! git merge --no-edit master; then
    echo
    if git rev-parse -q --verify MERGE_HEAD >/dev/null; then
      echo "git-sync: MERGE CONFLICT. Master is synced, but your branch is not pushed yet."
      echo "  Fix the files listed above, then run: git-save"
      echo "  Or cancel the merge with:             git merge --abort"
    else
      echo "git-sync: merge did not start, see the message above. Master is synced."
    fi
    return 1
  fi
  git push || return
  echo "git-sync: master and $branch are up to date."
}
# <<< 3kdb git helpers <<<
EOF
```

**2. Paste it into your terminal and press Enter.** Windows Terminal may warn that you're pasting several lines. That's fine, so choose **Paste anyway**.

This uses `cat` rather than `echo` because `echo` can't handle all the quote marks in this code. A backup of your old file is saved as `~/.bashrc.bak`.

**3. Load the helpers:**

```bash
source ~/.bashrc
```

**4. Check it worked:**

```bash
type git-sync
```

The first line should say `git-sync is a function`.

**Something went wrong?** This puts your old file back:

```bash
cp ~/.bashrc.bak ~/.bashrc
source ~/.bashrc
```

**On a Mac:** the helpers are written for `bash`, but Macs open `zsh` by default, which doesn't read `.bashrc`. Type `bash` and press Enter first in any terminal where you want to use them. They were tested on Linux and Windows (WSL), not on a Mac.

[Back to top](#3kdb-git-and-github-guide)

---

## Part 6: Everyday routine

Run these from the top of your folder. In a subfolder, `git-save` and `git-pr-pro` only pick up changes in that folder and below.

```bash
cd ~/3kdb
```

`fix-bard` below is an example branch name. Make up your own each time, using letters, numbers and dashes, with no spaces.

**1. Start a new branch from a fresh copy of the project:**

```bash
git-start fix-bard
```

**2. Make your changes.**

**3. Write your pull request description.** Paste your text, press Enter, then press `Ctrl+D`:

```bash
git-make-desc
```

**4. Send it.** This commits, pushes and opens the pull request:

```bash
git-pr-pro "PR title"
```

**5. Back to step 1 with a new branch name.**

That's all you need. `git-start` already updates `master`, so you don't need `git-sync` first, and `git-pr-pro` commits and pushes for you.

**Optional, during step 2:**

```bash
git-save "what I changed"
```

This backs up your work to your fork. Use it as often as you like.

```bash
git-sync
```

This pulls in the latest from the project.

**Things to watch for:**

- Use a new branch name each time. If the name already exists, `git-start` stops and changes nothing.
- `git-start` begins from `master`, so the new branch doesn't include work from a pull request that hasn't merged yet. See [Part 8](#part-8-open-pull-requests) if you need that code.
- Run `git-make-desc` before **every** pull request. If you skip it, `git-pr-pro` sends the description from your last one.
- `git-sync` doesn't make a new branch. It stays on the branch you're on.
- Save before `git-start`, or your unsaved changes come along to the new branch. If `master` has a different version of a file you edited, git refuses to switch and you stay where you are. Run `git-save`, then `git-start` again. `vars.tin` files are the exception, because `git-start` handles them.
- `git-save` and `git-sync` push to the branch you're on. If that branch has an open pull request, the changes join it.
- `git-save` and `git-pr-pro` commit new files in your folder too, including your character's folder if it's new. `private.tin` is left out, and so is `vars.tin` for a new character. To keep the whole folder out, see [Part 4, step 5](#part-4-switch-an-existing-clone-to-a-fork).

**Quick checks:**

```bash
git status
```

Shows which branch you're on and what's changed.

```bash
git branch
```

Lists your local branches.

[Back to top](#3kdb-git-and-github-guide)

---

## Part 7: What each helper does

### The ones you use

**`git-start <name>`**
- Updates `master` from the project, pushes it to your fork, then makes a new branch from it.
- Use it when starting something new that doesn't depend on an unmerged pull request.
- Safe while playing. Your `vars.tin` changes are kept.

**`git-save "message"`**
- Commits your changes and pushes the branch you're on. The message is optional, and the default is `savepoint`.
- Also use it to finish a merge after fixing a conflict.
- Doesn't touch `master` or bring in anything new. Includes `vars.tin` files, and refuses to run on `master`.

**`git-sync`**
- The "make everything up to date" command. From any branch, it:
  1. saves and pushes uncommitted work on your branch
  2. updates local `master` from the project
  3. pushes `master` to your fork, which clears "X commits behind" on GitHub
  4. merges `master` into your branch and pushes it
- If you had unsaved work, it makes a commit named `sync-<date>`. Run `git-save "real message"` first if you want a better name.

**`git-keep-vars <command>`**
- Runs a git command with your changed `vars.tin` files moved aside, then puts them back. If the game saves during the command, it tries again, up to 5 times.
- Use it when git complains about a `vars.tin` file while switching branches:
  ```bash
  git-keep-vars git checkout fix-bard
  ```
- Don't use it for `git-sync`. See [Part 9](#part-9-merge-conflicts).

**`git-make-desc`**
- Saves your pull request description to `~/3kdb-temp/pr.md`, overwriting the old one.
- Keep that folder name even if your repo folder has a different name. It's made for you, it sits outside your repo, and `git-pr-pro` looks for the file there.

**`git-pr-pro "PR title"`**
- Commits anything left, pushes, and opens a pull request to the project using your `git-make-desc` text.
- Use it when the work is ready, on a branch with no open pull request yet.

### The ones you can ignore

- **`git-sync-conflict`** is an older, weaker `git-sync`. It doesn't save or push anything.
- **`git-pr "message"`** is an older `git-pr-pro`. It has a canned description.
- **`git-work <name>`** makes a new branch from wherever you are, with no updating. It's only for building on an unmerged pull request.

### git-save or git-sync?

- `git-save` sends **my** work up to GitHub.
- `git-sync` does the same, **and** gets everyone else's work and updates everything.

`git-save` lets you name the commit, and it can't cause a merge conflict because it brings nothing in. `git-sync` names the commit `sync-<date>` and can hit a conflict.

[Back to top](#3kdb-git-and-github-guide)

---

## Part 8: Open pull requests

A pull request follows its branch. Anything pushed to that branch joins the pull request. After `git-pr-pro`, don't keep working on that branch unless you want the changes added to it.

**To change an open pull request:** switch to its branch, make the fix, and save. Don't run `git-pr-pro` again, because the pull request already exists.

```bash
git checkout fix-bard
git-save "fixed the thing"
```

**New work while one is waiting, not needing its code:**

```bash
git-start new-bot
```

**New work that needs the waiting one's code.** Run this from the waiting pull request's branch:

```bash
git-work new-bot
```

If you used `git-work`, the new branch contains the waiting commits. Wait for that pull request to merge, run `git-sync`, and **then** run `git-pr-pro`. Otherwise the new pull request also shows everything from the old one.

[Back to top](#3kdb-git-and-github-guide)

---

## Part 9: Merge conflicts

A conflict means you and the project changed the same lines, and git wants you to choose. Nothing is lost. Git shows both versions in the file:

```text
<<<<<<< HEAD
your version
=======
the project's version
>>>>>>> master
```

**Fix it:**

1. Open each file git listed, and search for `<<<<<<<`.
2. Edit it so it says what you want. That can be yours, theirs, or a mix.
3. Delete the `<<<<<<<`, `=======` and `>>>>>>>` lines.
4. Finish, using the commands for your setup below.

**With a fork, finish with:**

```bash
git-save "fix merge conflict"
```

**With a plain clone, finish with:**

```bash
git add .
git commit --no-edit
```

**Would you rather keep one whole version of a file?** Replace the path with your file, then finish as above.

Keep **your** version:

```bash
git checkout --ours -- common/example.tin
```

Keep **the project's** version:

```bash
git checkout --theirs -- common/example.tin
```

**Changed your mind?** This cancels the merge and puts things back:

```bash
git merge --abort
```

### When git-sync stops

**`MERGE CONFLICT`**

`master` is already synced, and only your branch is waiting. Follow the steps above.

**`a merge is still in progress`**

You have an unfinished conflict. Follow the steps above.

**`merge did not start`**

Usually a `vars.tin` you changed locally was also changed by the project. This works whether or not you're playing:

```bash
cp chars/byron/vars.tin ~/3kdb-temp/my-vars.tin
git checkout HEAD -- chars/byron/vars.tin
git-sync
cp ~/3kdb-temp/my-vars.tin chars/byron/vars.tin
```

If it says the same thing again, the game saved at that moment, so start over from the first line. Avoid `git stash` for this while playing. The game rewrites the file straight away, so `git stash pop` refuses to run, and it also sweeps up your other unsaved work.

**`you are on master`** (from `git-save`)

`master` should only hold what the project has. Your changes are safe and still there. Make a branch, then save:

```bash
git-start my-changes
git-save "my changes"
```

### vars.tin files

`vars.tin` is where a character's settings are saved. `git-save`, `git-sync` and `git-pr-pro` include changed `chars/*/vars.tin` files in commits, so they go with your pull request. That covers characters already in the project. A new character's `vars.tin` is ignored by git, so it stays on your computer.

The game keeps rewriting the file, so it shows as modified again in `git status` soon after a commit. That's normal.

[Back to top](#3kdb-git-and-github-guide)

---

## Part 10: Playing while using git

You can use all of the helpers while logged in. Two things are worth knowing.

**1. Switching branches changes the files on disk, but not your running game.**

- What's already loaded in the game stays as it was.
- Anything loaded after the switch (relog, `#read`) comes from the new branch, so a `#read` mid-game can leave you with a mix of both.
- To get a branch's changes, be on that branch **and** relog or `#read` the changed file.
- `git-start` begins from `master`, so relogging on the new branch drops anything from a pull request that hasn't merged yet. Switch back to that branch to get those features again.

**2. The game keeps rewriting `chars/<you>/vars.tin`.** If that file also differs between two branches, git refuses to switch:

```text
Your local changes to the following files would be overwritten
```

- `git-start` deals with this for you.
- Plain `git checkout` doesn't, so use this instead:
  ```bash
  git-keep-vars git checkout fix-bard
  ```
- `git-sync` doesn't either. See `merge did not start` in [Part 9](#part-9-merge-conflicts).
- Nothing is lost when git refuses. You just stay on the branch you're on.

If `git-keep-vars` or `git-start` says it couldn't put `vars.tin` back, your copy is in a `~/3kdb-temp/vars-backup.*` folder.

[Back to top](#3kdb-git-and-github-guide)

---

## Part 11: Problems and fixes

**`git-sync: command not found`** (or any other helper)

The helpers aren't installed, or this terminal hasn't loaded them. Run this, and if that doesn't help, do [Part 5](#part-5-install-the-git-helpers):

```bash
source ~/.bashrc
```

**`Your local changes to the following files would be overwritten by merge`**

See [Keep your changes and still update](#keep-your-changes-and-still-update).

**`fatal: Need to specify how to reconcile divergent branches`**

You have your own commits, and the project has new ones too. Use this instead of plain `git pull`:

```bash
git pull --no-rebase --no-edit
```

**`Author identity unknown`** or **`Please tell me who you are`**

Tell git your name and email, then run your command again:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**`Permission to jmitchell33/3kdb.git denied`**

You're on a plain clone, so you can't push to the main project. Switch to a fork with [Part 4](#part-4-switch-an-existing-clone-to-a-fork).

**Git asks for a username and password, or says password authentication isn't supported**

Log in with the GitHub tool, and answer **Yes** to "authenticate Git":

```bash
gh auth login
```

**`git-start: a branch named ... already exists`**

Pick a new name. Nothing was changed.

**`Not possible to fast-forward`** or `master` is `rejected` when syncing

Your local `master` has commits of its own. Move them to a branch with [Part 4, step 5](#part-4-switch-an-existing-clone-to-a-fork), then run `git-sync`.

**`upstream` is missing from `git remote -v`**

```bash
git remote add upstream https://github.com/jmitchell33/3kdb.git
```

**GitHub says my fork is "X commits behind"**

```bash
git-sync
```

**`Error: Could not find PR description file`**

Run `git-make-desc` first.

**My `.bashrc` looks wrong after pasting**

Restore the backup, as shown in [Part 5](#part-5-install-the-git-helpers).

[Back to top](#3kdb-git-and-github-guide)
