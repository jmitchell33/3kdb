# 3kdb Setup Guide

This guide takes you from nothing to playing 3Kingdoms with 3kdb.

**Byron is the example player here.** Wherever you see `byron`, use your own character's name, in lower case.

Anything in a grey box is something to type or paste. On GitHub, a copy button appears in the corner of the box when you hover over it or tap it. If you don't see one, select the text and copy it.

**Other guides:** [manual.md](manual.md) explains everything 3kdb can do, [faq.md](faq.md) has short answers, and [github.md](github.md) covers git and GitHub.

## Contents

**Getting started**
- [Step 1: Install TinTin++ and git](#step-1-install-tintin-and-git)
- [Step 2: Download 3kdb](#step-2-download-3kdb)
- [Step 3: Open the menu](#step-3-open-the-menu)
- [Step 4: Add your character](#step-4-add-your-character)
- [Step 5: Log in](#step-5-log-in)
- [Step 6: Finish setup in the game](#step-6-finish-setup-in-the-game)

**After that**
- [Playing from now on](#playing-from-now-on)
- [Using the menu](#using-the-menu)
- [Getting updates](#getting-updates)
- [What the menu creates for you](#what-the-menu-creates-for-you)
- [Already using 3k.tin?](#already-using-3ktin)
- [Problems and fixes](#problems-and-fixes)

---

## Step 1: Install TinTin++ and git

**TinTin++** is the program you play through. Do **not** install it with `apt-get`, because that version is very far behind. Follow the instructions for your system here:

https://tintin.mudhalla.net/install.php

On Windows, you'll be working in Ubuntu, a Linux terminal that runs inside Windows. To install it:

1. Open the Start menu, type `PowerShell`, right-click it and pick **Run as administrator**.
2. Run this, then restart your PC when it finishes:
   ```
   wsl --install
   ```
3. Open **Ubuntu** from the Start menu and make a username and password. The password stays invisible while you type. That's normal.

Do everything else in this guide inside that Ubuntu window.

When TinTin++ is installed, check that it works. You should see a version number:

```bash
tt++ -V
```

Then check for **git**:

```bash
git --version
```

If it says `command not found`, install it on Ubuntu or Debian with:

```bash
sudo apt update
sudo apt install -y git
```

**How to paste into a terminal:** right-click, or press `Ctrl+Shift+V`. Plain `Ctrl+V` usually doesn't work. Press Enter after each command.

[Back to top](#3kdb-setup-guide)

---

## Step 2: Download 3kdb

Pick **one** option.

- **Option A:** you just want to play and get updates. No GitHub account needed.
- **Option B:** you want to send your own changes to the project. Needs a free GitHub account.

Not sure? Pick A. You can [switch to B later](github.md#part-4-switch-an-existing-clone-to-a-fork) without losing anything.

### Option A: Just play

```bash
cd ~
git clone https://github.com/jmitchell33/3kdb.git
```

You now have a folder called `3kdb` in your home folder.

### Option B: Make your own fork

A fork is your own copy of the project on GitHub. First [make a GitHub account](https://github.com/signup), then run these one at a time. Use your own name and GitHub email, and keep the quotes.

```bash
sudo apt update
sudo apt install -y git gh
```

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global push.autoSetupRemote true
```

```bash
gh auth login
```

For `gh auth login`, pick **GitHub.com**, **HTTPS**, **Yes** (authenticate Git), and **Login with a web browser**.

```bash
cd ~
gh repo fork jmitchell33/3kdb --clone
```

You now have a folder called `3kdb` in your home folder, linked to your fork. For more detail, and the helper commands that make this easier, see [Part 3 of github.md](github.md#part-3-set-up-a-fork-from-scratch).

[Back to top](#3kdb-setup-guide)

---

## Step 3: Open the menu

```bash
cd ~/3kdb
tt++ startmenu.tin
```

You'll see:

```text
  ██████╗ ██╗  ██╗██████╗ ██████╗
  ╚════██╗██║ ██╔╝██╔══██╗██╔══██╗
   █████╔╝█████╔╝ ██║  ██║██████╔╝
   ╚═══██╗██╔═██╗ ██║  ██║██╔══██╗
  ██████╔╝██║  ██╗██████╔╝██████╔╝
  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═════╝
  A community project, built by many players of 3Kingdoms.

  Choose a character

  No characters yet

  [ Add ]  [ Log in as guest ]  [ Quit ]
```

On a small screen, or with a long character list, the logo shrinks to one line and the list scrolls.

You must be inside the `3kdb` folder when you run `tt++ startmenu.tin`. The `cd` line above takes care of that.

## Step 4: Add your character

1. `[ Add ]` is already highlighted, so press **Enter**.
2. It asks for your character name. Type it and press Enter:
   ```text
   byron
   ```
3. It asks for your guild. Type it and press Enter:
   ```text
   bard
   ```
   - No guild yet? Type `adventurer`.
   - In more than one guild? List them with spaces, default first: `bard mage`.
   - To see the guild names 3kdb supports, run this in another terminal: `ls ~/3kdb/common/guilds`
4. It asks for your password. You have two choices:
   - Type it and press Enter, and the menu logs you in with it from now on. **It shows on screen while you type**, and it's saved as plain text in `chars/byron/private.tin`. That file is never uploaded by git.
   - Just press Enter to save nothing, and type your password at each login.

Byron now appears in the list. The menu has made everything the character needs, so there's no copying or editing to do.

## Step 5: Log in

With your character highlighted, press **Enter**. You can also press its number, such as `1`.

**Brand new to 3k?** If that name isn't on the game yet, it asks `Would you like to create this character`. Check the spelling, because this makes a real character, then type `y` and press Enter. Your saved password is used for you. If you didn't save one, type the password you want, twice.

The game then asks a few more questions. Type each answer and press Enter:

- **Male or female**
- **Your email address**, and whether players can see it
- **Where you heard about 3Kingdoms**
- **Whether you can see ANSI colours.** Type `y`, which suits nearly every terminal.
- **Whether you want a hardcore character.** Type `no` unless you're sure, because one death means that character can no longer advance or leave town. `help hardcore` explains it.
- **Whether you agree to the game's terms**

3kdb then loads as usual, and the game offers a tutorial. Type `yes` or `no`. The game warns that level 1 characters aren't saved when you quit, and `help purge` says one that doesn't log in for 2 weeks is purged. Getting to level 2 only takes 300 more experience, from killing a few monsters.

**3k only allows one character per player until level 50**, and extra ones have to be registered. Breaking this can get your characters removed, so read `help characters` before making a second one.

If you didn't save a password, type it when the game asks.

## Step 6: Finish setup in the game

Do this **once per character**, the first time you're logged in. Type these into the game, pressing Enter after each:

```text
setup_3kdb
```

This sets the game options 3kdb needs for mapping, triggers and other features.

```text
setup_3kdb_hpbar
```

This sets up your guild's HP bar. Not every guild has one. If the game says `There is no reason to...`, your guild doesn't have one, so skip it.

**Bards:** 3kdb assumes you also have this setting on:

```text
bset auto_shield 1
```

**That's it. Enjoy!** Good next commands to try in the game:

- `dblib` lists the aliases
- `mapgo cot` sets your map position to Center of Town
- `botlist`, `speedruns` and `strategies` show what else is available

[Back to top](#3kdb-setup-guide)

---

## Playing from now on

```bash
cd ~/3kdb
tt++ startmenu.tin
```

Pick your character and press Enter. To go back to the menu, type `ld` in the game. Your character stays linkdead and keeps its equipment. `quit` also goes back to the menu, but it logs you out fully and you can lose equipment. See [Leaving the game](manual.md#leaving-the-game).

## Using the menu

**On the character list**
- **Up / Down:** pick a character
- **Left / Right:** change guild, if you listed more than one
- **Enter:** log in
- **1 to 9:** log in directly. With 10 or more characters, or if the list doesn't all fit on your screen, type the number and then press Enter.
- **Page Up / Page Down:** move a screenful, if the list doesn't all fit
- **Tab:** jump to the Edit and Remove buttons
- **q:** close the program

**On the button row**
- **Left / Right:** pick a button, then press **Enter**
- **Add:** add another character
- **Edit:** change a character's guild list
- **Remove:** take a character off the menu. Its files are kept.
- **Log in as guest:** play straight away with no character or password. The game doesn't save guests.

You can also click names, guild arrows and buttons. Hold **Shift** to select text while the menu is showing.

The list shows as many characters as your screen has room for and scrolls as you move. `▲ 3 above   ▼ 5 below` under it shows how many are hidden. You can tap or click that row to page through the list, or use the mouse wheel.

To change guild while logged in, use `gswap` as usual, such as `gswap mage`. 3kdb reloads its scripts for the new guild and remembers it for next time.

## Getting updates

**Option A (just play):**

```bash
cd ~/3kdb
git pull
```

**Option B (fork), once you've [installed the helpers](github.md#part-5-install-the-git-helpers):**

```bash
cd ~/3kdb
git-sync
```

If you're logged in, log out and back in to load the new code.

Did it stop with an error because you changed some files? See [Keep your changes and still update](github.md#keep-your-changes-and-still-update).

## What the menu creates for you

Each time it opens, the menu makes these folders if they're missing:

- `logs/<your system username>/chatlogs/` for your chat logs, and `logs/<your system username>/discord/` for Discord posting
- `vars/` for the reboot times shown on the menu

When you add a new character, it makes:

- `chars/byron/byron.tin`, the main character file, already filled in with your name and guild
- `chars/byron/guild.tin`, your current guild
- `chars/byron/vars.tin`, your saved settings
- `chars/byron/private.tin`, your password and other secrets
- `chars/byron/actions.tin`, `aliases.tin`, `config.tin`, `heartbeat.tin`, `miphp.tin` and `tickers.tin`, which are your own custom code files

The character list itself is saved in `chars/startmenu_data.tin`.

[Back to top](#3kdb-setup-guide)

---

## Already using 3k.tin?

You don't need `3k.tin` any more. Older instructions used it, but the menu replaces it and is easier. Moving over takes a minute and keeps your character's files.

1. Open the menu:
   ```bash
   cd ~/3kdb
   tt++ startmenu.tin
   ```
2. Highlight `[ Add ]` and press Enter.
3. Type your character's name and press Enter.
4. Your guild is already filled in, so press Enter.

It won't ask for a password here, because the character already exists. To have the menu log you in automatically, close the menu with `q` and run this, using your own name and password. Keep the single quotes and braces:

```bash
cd ~/3kdb
echo '#var PASSWORD {yourpassword};' >> chars/byron/private.tin
```

Your password won't be sent upstream. Git ignores `private.tin`, so it stays on your computer, and the game's saved settings in `vars.tin` don't include it.

## Problems and fixes

**`tt++: command not found`**

TinTin++ isn't installed, or it didn't finish installing. Go back to [Step 1](#step-1-install-tintin-and-git).

**I see the TinTin++ welcome screen instead of the menu**

You aren't in the `3kdb` folder. Type `#end` and press Enter to close it, then run:

```bash
cd ~/3kdb
tt++ startmenu.tin
```

**The menu says "No characters yet" but I added some**

Same cause. Press `q`, then run the two commands above.

**`#NO SESSION ACTIVE`**

You typed a game command while not connected. You're probably in plain TinTin++, so see the welcome screen fix above.

**`#ERROR: #LINE LOG {logs/...}: COULDN'T OPEN FILE`**

Your log folder is missing. Opening the menu creates it. If you logged in another way, run:

```bash
cd ~/3kdb
mkdir -p "logs/$(whoami)/chatlogs" "logs/$(whoami)/discord" vars
```

**`3kdb has no scripts for: ...`**

The menu doesn't recognise that guild name. Check the spelling against this list, then type it again:

```bash
ls ~/3kdb/common/guilds
```

**`Names are letters only`**

Character names can only contain letters, with no numbers or spaces.

**Add didn't ask for my password**

A folder with that name already exists in `chars/`, so the menu used it instead of making a new one. That's expected if the character is already yours. Add the password with the `echo` command under [Already using 3k.tin?](#already-using-3ktin).

**I saved the wrong password**

Open the file and fix the `#var PASSWORD` line near the bottom. Press `Ctrl+O`, Enter, then `Ctrl+X` to save and exit.

```bash
nano ~/3kdb/chars/byron/private.tin
```

**The screen looks broken or squashed**

Make your terminal window bigger. 3kdb redraws when the window size changes, and it switches to a phone layout when the window is 75 columns wide or less.

**I can't select text in the menu**

Hold **Shift** while selecting.

**`fatal: destination path '3kdb' already exists`**

You've already downloaded it. To update instead, see [Getting updates](#getting-updates).

**`Permission denied` when opening or saving files**

Something was probably run with `sudo`, which made those files belong to the admin account. None of these steps need `sudo` for files inside `3kdb`, including `nano`. To fix it:

```bash
sudo chown -R "$(whoami):" ~/3kdb
```

**`git pull` stops with an error**

See [Keep your changes and still update](github.md#keep-your-changes-and-still-update).

[Back to top](#3kdb-setup-guide)
