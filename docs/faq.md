# 3kdb FAQ

Short answers to common questions and problems. For the full explanation of how things work, see the [manual](manual.md).

Anything in a grey box is something to type or paste. `byron` is an example, so use your own character's name.

**Other guides:** [manual.md](manual.md), [setup.md](setup.md), [github.md](github.md)

## Contents

- [Getting started](#getting-started)
  - [What is 3kdb?](#what-is-3kdb)
  - [Do I need a GitHub account?](#do-i-need-a-github-account)
  - [Do I need to know how to code?](#do-i-need-to-know-how-to-code)
  - [How do I install it?](#how-do-i-install-it)
  - [Can I install TinTin++ with apt-get?](#can-i-install-tintin-with-apt-get)
  - [Does it work on Windows?](#does-it-work-on-windows)
  - [Can I play on a phone?](#can-i-play-on-a-phone)
  - [How do I start the game each time?](#how-do-i-start-the-game-each-time)
  - [Do I still need 3k.tin?](#do-i-still-need-3ktin)
  - [Can I rename the 3kdb folder?](#can-i-rename-the-3kdb-folder)
  - [Do I need to make folders or copy a template?](#do-i-need-to-make-folders-or-copy-a-template)
  - [What do I run after my first login?](#what-do-i-run-after-my-first-login)
  - [What setting do bards need?](#what-setting-do-bards-need)
- [The start menu](#the-start-menu)
  - [How do I add another character?](#how-do-i-add-another-character)
  - [What do I type for guild if I don't have one?](#what-do-i-type-for-guild-if-i-dont-have-one)
  - [I'm in more than one guild. What do I do?](#im-in-more-than-one-guild-what-do-i-do)
  - [Is my saved password safe?](#is-my-saved-password-safe)
  - [How do I change my saved password?](#how-do-i-change-my-saved-password)
  - [Add didn't ask for my password. Why?](#add-didnt-ask-for-my-password-why)
  - [Does Remove delete my character?](#does-remove-delete-my-character)
  - [What does the linkdead timer on the menu mean?](#what-does-the-linkdead-timer-on-the-menu-mean)
  - [How do I refresh my linkdead timers?](#how-do-i-refresh-my-linkdead-timers)
  - [Why don't I see the next reboot time?](#why-dont-i-see-the-next-reboot-time)
  - [The menu says "No characters yet", but I've added some](#the-menu-says-no-characters-yet-but-ive-added-some)
  - [I see the TinTin++ welcome screen instead of the menu](#i-see-the-tintin-welcome-screen-instead-of-the-menu)
  - [It says "3kdb has no scripts for"](#it-says-3kdb-has-no-scripts-for)
  - [It says "Names are letters only"](#it-says-names-are-letters-only)
  - [I can't select text in the menu](#i-cant-select-text-in-the-menu)
- [Playing](#playing)
  - [How do I find a command?](#how-do-i-find-a-command)
  - [How do I walk somewhere?](#how-do-i-walk-somewhere)
  - [The map is showing the wrong place](#the-map-is-showing-the-wrong-place)
  - [How do I log out?](#how-do-i-log-out)
  - [How do I close the whole program?](#how-do-i-close-the-whole-program)
  - [How do I scroll back?](#how-do-i-scroll-back)
  - [Why does pressing Enter repeat my last command?](#why-does-pressing-enter-repeat-my-last-command)
  - [The game shows "More:" and seems stuck](#the-game-shows-more-and-seems-stuck)
  - [How do I run two commands at once?](#how-do-i-run-two-commands-at-once)
  - [How do I use the mouse?](#how-do-i-use-the-mouse)
  - [How do I change colours?](#how-do-i-change-colours)
  - [How do I hide the map?](#how-do-i-hide-the-map)
  - [How do I hide combat spam?](#how-do-i-hide-combat-spam)
  - [How do I turn a feature on or off?](#how-do-i-turn-a-feature-on-or-off)
  - [How do I change guild?](#how-do-i-change-guild)
  - [Where are my chat logs?](#where-are-my-chat-logs)
  - [How do I hide someone from my chat window?](#how-do-i-hide-someone-from-my-chat-window)
  - [How do I post my chat to Discord?](#how-do-i-post-my-chat-to-discord)
  - [What is a wizard?](#what-is-a-wizard)
- [Bots and the deadman timer](#bots-and-the-deadman-timer)
  - [Are bots allowed?](#are-bots-allowed)
  - [How do I start a bot?](#how-do-i-start-a-bot)
  - [How do I stop a bot?](#how-do-i-stop-a-bot)
  - [How do I pause a bot?](#how-do-i-pause-a-bot)
  - [My bot stopped and I don't know why](#my-bot-stopped-and-i-dont-know-why)
  - [The bot wants me to press 1, 2 or 3](#the-bot-wants-me-to-press-1-2-or-3)
  - [The bot walked the wrong way](#the-bot-walked-the-wrong-way)
  - [Can I run several bots in a row?](#can-i-run-several-bots-in-a-row)
  - [What's the deadman timer?](#whats-the-deadman-timer)
  - [My bot paused and it says DEADMAN TIMEOUT](#my-bot-paused-and-it-says-deadman-timeout)
  - [Can I make a timer that stops me going idle?](#can-i-make-a-timer-that-stops-me-going-idle)
- [Making your own commands](#making-your-own-commands)
  - [Where do I put my own aliases?](#where-do-i-put-my-own-aliases)
  - [Where do I put my own actions?](#where-do-i-put-my-own-actions)
  - [What's the difference between an alias and an action?](#whats-the-difference-between-an-alias-and-an-action)
  - [What editor should I use?](#what-editor-should-i-use)
  - [How do I open my files from Windows?](#how-do-i-open-my-files-from-windows)
  - [I saved my alias, but it doesn't work](#i-saved-my-alias-but-it-doesnt-work)
  - [My action doesn't fire](#my-action-doesnt-fire)
  - [My action keeps firing forever](#my-action-keeps-firing-forever)
  - [Will an update overwrite my aliases?](#will-an-update-overwrite-my-aliases)
  - [Should I edit common/ or modules/?](#should-i-edit-common-or-modules)
  - [Which files shouldn't I edit?](#which-files-shouldnt-i-edit)
  - [What does #NOP do?](#what-does-nop-do)
- [Updating and git](#updating-and-git)
  - [How do I get updates?](#how-do-i-get-updates)
  - [Clone or fork?](#clone-or-fork)
  - [I cloned already and now want a fork](#i-cloned-already-and-now-want-a-fork)
  - [How do I install the git helpers?](#how-do-i-install-the-git-helpers)
  - [What do I do when git says my changes would be overwritten?](#what-do-i-do-when-git-says-my-changes-would-be-overwritten)
  - [What's a merge conflict, and how do I fix it?](#whats-a-merge-conflict-and-how-do-i-fix-it)
  - [What's the difference between git-save and git-sync?](#whats-the-difference-between-git-save-and-git-sync)
  - [Why does vars.tin always show as changed?](#why-does-varstin-always-show-as-changed)
  - [git-sync: command not found](#git-sync-command-not-found)
  - [fatal: Need to specify how to reconcile divergent branches](#fatal-need-to-specify-how-to-reconcile-divergent-branches)
  - [Author identity unknown](#author-identity-unknown)
  - [Permission to jmitchell33/3kdb.git denied](#permission-to-jmitchell333kdbgit-denied)
  - [Git asks for a username and password](#git-asks-for-a-username-and-password)
  - [fatal: destination path '3kdb' already exists](#fatal-destination-path-3kdb-already-exists)
  - [More git problems](#more-git-problems)
- [Errors and problems](#errors-and-problems)
  - [tt++: command not found](#tt-command-not-found)
  - [#NO SESSION ACTIVE](#no-session-active)
  - [#ERROR: #LINE LOG {logs/...}: COULDN'T OPEN FILE](#error-line-log-logs-couldnt-open-file)
  - [There is no reason to '...' here](#there-is-no-reason-to--here)
  - [The screen looks broken or squashed](#the-screen-looks-broken-or-squashed)
  - [I see $eternal_string on the screen](#i-see-eternal_string-on-the-screen)
  - [Permission denied when saving files](#permission-denied-when-saving-files)
  - [Where do I get more help?](#where-do-i-get-more-help)

---

## Getting started

### What is 3kdb?

It's a set of TinTin++ scripts for playing 3Kingdoms. It adds a map, chat window, bots, trackers, guild tools, and a place for your own commands. See [What is 3kdb?](manual.md#what-is-3kdb).

### Do I need a GitHub account?

Not to play or get updates. You only need one to send changes to the project. See [Which one do I need?](github.md#part-1-which-one-do-i-need).

### Do I need to know how to code?

No. You can use everything without coding. If you'd like to make your own commands, the manual [walks you through it](manual.md#making-your-own-commands).

### How do I install it?

Follow [setup.md](setup.md). The short version, once TinTin++ and git are installed:

```bash
cd ~
git clone https://github.com/jmitchell33/3kdb.git
cd 3kdb
tt++ startmenu.tin
```

### Can I install TinTin++ with apt-get?

No. That version is very far behind. Use https://tintin.mudhalla.net/install.php instead.

### Does it work on Windows?

Yes, through Ubuntu, a Linux terminal that runs inside Windows. [setup.md Step 1](setup.md#step-1-install-tintin-and-git) shows how to install it.

### Can I play on a phone?

3kdb has a phone layout, which switches on when your terminal is 75 columns wide or less. You still need a terminal on your phone that's connected to a machine with 3kdb installed.

### How do I start the game each time?

```bash
cd ~/3kdb
tt++ startmenu.tin
```

### Do I still need 3k.tin?

No. The menu replaces it. If you've been using `3k.tin`, [moving over](setup.md#already-using-3ktin) takes a minute and keeps your character's files.

### Can I rename the 3kdb folder?

Yes. Just use your new name wherever the guides say `~/3kdb`. Keep `~/3kdb-temp` as it is, though, because the git helpers look there.

### Do I need to make folders or copy a template?

No. The menu creates all of it. See [what it creates](setup.md#what-the-menu-creates-for-you).

### What do I run after my first login?

Run these once per character:

```text
setup_3kdb
setup_3kdb_hpbar
```

### What setting do bards need?

3kdb assumes bards have this on:

```text
bset auto_shield 1
```

[Back to top](#3kdb-faq)

---

## The start menu

### How do I add another character?

Highlight `[ Add ]` with the arrow keys and press Enter. You can also click it.

### What do I type for guild if I don't have one?

Type `adventurer`.

### I'm in more than one guild. What do I do?

List them with spaces when you add the character, default first: `bard mage`. Then use **Left** and **Right** on the menu to pick one. To change the list later, use the `[ Edit ]` button.

### Is my saved password safe?

It's saved as plain text in `chars/byron/private.tin`. Git never uploads that file, but anyone who can open your files can read it. If you share a computer, leave the password empty and type it at each login.

### How do I change my saved password?

Open the file and fix the `#var PASSWORD` line near the bottom. Save with `Ctrl+O`, Enter, then `Ctrl+X`.

```bash
nano ~/3kdb/chars/byron/private.tin
```

### Add didn't ask for my password. Why?

A folder with that name already exists in `chars/`, so the menu used it. To add a password to it, run this with your own name and password. Keep the single quotes and braces:

```bash
cd ~/3kdb
echo '#var PASSWORD {yourpassword};' >> chars/byron/private.tin
```

### Does Remove delete my character?

No. It only takes the character off the menu, and the files stay. Your game character isn't affected either.

### What does the linkdead timer on the menu mean?

You left that character linkdead, and it shows how long until the game boots it. Without the linkdead perk, that's 24 hours. With it, only a reboot does.

### How do I refresh my linkdead timers?

Press **0** twice quickly on the menu.

### Why don't I see the next reboot time?

It appears after a character has logged in once.

### The menu says "No characters yet", but I've added some

You aren't in the `3kdb` folder. Press `q`, then run:

```bash
cd ~/3kdb
tt++ startmenu.tin
```

### I see the TinTin++ welcome screen instead of the menu

You aren't in the `3kdb` folder. Type `#end` and press Enter, then run the two commands above.

### It says "3kdb has no scripts for"

The menu doesn't recognise that guild name. Check the spelling against this list:

```bash
ls ~/3kdb/common/guilds
```

### It says "Names are letters only"

Character names can only contain letters, with no numbers or spaces.

### I can't select text in the menu

Hold **Shift** while selecting.

[Back to top](#3kdb-faq)

---

## Playing

### How do I find a command?

Use `dblib`, or `dblib` plus a type or your guild's name. `dbinfo <command>` gives details on one. See [Finding commands](manual.md#finding-commands).

```text
dblib bard
```

```text
dbinfo go
```

### How do I walk somewhere?

`speedruns` lists the places, and `go` walks you there:

```text
go shop
```

### The map is showing the wrong place

```text
findhere
```

If that can't tell which room you're in, try:

```text
findhere-auto
```

### How do I log out?

`quit` logs out properly, and `ld` leaves your character linkdead. See [Leaving the game](manual.md#leaving-the-game).

### How do I close the whole program?

Press `q` on the menu. In plain TinTin++, type `#end`.

### How do I scroll back?

Use **Page Up** and **Page Down**. You can also search with `grep`:

```text
grep hello
```

### Why does pressing Enter repeat my last command?

That's how 3kdb is set up. Pressing Enter on an empty line repeats what you last typed.

### The game shows "More:" and seems stuck

It's waiting at a long help page. Press Enter for the next page, or `q` to stop.

### How do I run two commands at once?

Put `;` between them:

```text
say one;say two
```

### How do I use the mouse?

Type `qq` to turn it on or off. Turn it off to select text normally.

### How do I change colours?

`themes` lists them, and `theme <name>` switches. You may need to run `ld` and log back in to see all of it.

```text
theme bright
```

### How do I hide the map?

Type `hidemap`, and the data panel moves up into its space. `go`, `findhere` and bots still work. Type `showmap` to bring it back. It's saved for each character, and the map shows by default.

### How do I hide combat spam?

`gags` lists what you can hide. To hide a group:

```text
gag+ combat_generic
```

### How do I turn a feature on or off?

`toggle-list` shows them all, and `toggle <name>` flips one.

### How do I change guild?

Use `gswap <guild>` as usual, and 3kdb follows. You need the perk for it in the game.

### Where are my chat logs?

In `logs/<your system username>/`, inside your `3kdb` folder.

### How do I hide someone from my chat window?

```text
blacklist+ <name>
```

### How do I post my chat to Discord?

The manual has [the steps](manual.md#sending-chat-to-discord).

### What is a wizard?

A wizard is a staff member of the game. If you need help with a game problem, you can ask one.

[Back to top](#3kdb-faq)

---

## Bots and the deadman timer

### Are bots allowed?

Most scripting is allowed, but you must be present and able to respond while you're advancing your character. Leaving automation running while you're away isn't allowed. Read the rules, and ask a wizard if you're not sure:

```text
help rules
```

### How do I start a bot?

`botlist` shows them. `+` walks to the start and begins, and `-` checks first:

```text
+turkeys
```

### How do I stop a bot?

```text
.stop
```

### How do I pause a bot?

`.pause` pauses it, and `.unpause` continues. `.resume` walks back to where you paused, then continues.

### My bot stopped and I don't know why

Check that you aren't paused, or that the deadman didn't fire. To tell the bot to walk on:

```text
..
```

### The bot wants me to press 1, 2 or 3

You aren't in its start room. Press **1** to run there, **2** if you're in the right room but the map needs moving, or **3** to run it anyway. The choice lasts 5 seconds.

### The bot walked the wrong way

The map probably doesn't match where you are. Pause the bot, then run `findhere`.

### Can I run several bots in a row?

Yes, with the bot cycler. See [Run several areas in a row](manual.md#run-several-areas-in-a-row).

### What's the deadman timer?

A safety switch. If you don't type anything for 15 minutes, it pauses your bot. Typing anything resets the countdown. See [Deadman timer](manual.md#deadman-timer).

### My bot paused and it says DEADMAN TIMEOUT

You didn't type for the length of the timer. Check everything's safe, then continue:

```text
.unpause
```

If it doesn't start moving again, type `..`.

### Can I make a timer that stops me going idle?

No. The game's rules ban triggers or timers that just keep you from going idle.

[Back to top](#3kdb-faq)

---

## Making your own commands

### Where do I put my own aliases?

In `chars/byron/aliases.tin`, between the `#class ... open` and `#class ... close` lines. The manual has [a full walkthrough](manual.md#your-first-alias).

### Where do I put my own actions?

In `chars/byron/actions.tin`, in the same place. See [Your first action](manual.md#your-first-action).

### What's the difference between an alias and an action?

You run an alias by typing its name. An action runs by itself when certain text appears in the game.

### What editor should I use?

Whichever you like. `nano` is built in and simple, VS Code is the most popular for bigger jobs, and Notepad++ is good on Windows. See [Pick an editor](manual.md#pick-an-editor).

### How do I open my files from Windows?

```bash
cd ~/3kdb
explorer.exe .
```

### I saved my alias, but it doesn't work

The game only sees your change after you reload:

```text
.reload
```

If it still doesn't work, look for a missing `;` or `}`. See [If something doesn't work](manual.md#if-something-doesnt-work).

### My action doesn't fire

Check the pattern matches the game's text exactly. Only one action fires per line of text, so 3kdb may have one on that line already. A priority can put yours first. See [Be careful with actions](manual.md#be-careful-with-actions).

### My action keeps firing forever

It's setting itself off. Type this and press Enter to remove all your actions, then fix the file and run `.reload`:

```text
#class {player_actions} {kill}
```

### Will an update overwrite my aliases?

Your own character's folder stays where it is when you update. If that folder also exists in the project, see [Keep your changes and still update](github.md#keep-your-changes-and-still-update).

### Should I edit common/ or modules/?

Keep your own code in your character's folder if you can. Changes in `common/` and `modules/` can clash with updates. If you've fixed something that would help everyone, you can [send it in](github.md#part-6-everyday-routine).

### Which files shouldn't I edit?

`vars.tin`, because the game rewrites it, and `guild.tin`, because the menu and `gswap` write it.

### What does #NOP do?

Nothing. It marks a line as a comment, so you can leave notes for yourself. End it with `;`.

[Back to top](#3kdb-faq)

---

## Updating and git

### How do I get updates?

**If you only cloned:**

```bash
cd ~/3kdb
git pull
```

**If you have a fork:**

```bash
cd ~/3kdb
git-sync
```

Then run `.reload`, or log back in.

### Clone or fork?

Clone if you only want to play. Fork if you want to send in changes. You can [switch to a fork later](github.md#part-4-switch-an-existing-clone-to-a-fork) without losing anything.

### I cloned already and now want a fork

Follow [Part 4 of github.md](github.md#part-4-switch-an-existing-clone-to-a-fork). You don't need to download anything again.

### How do I install the git helpers?

Follow [Part 5 of github.md](github.md#part-5-install-the-git-helpers). It's one paste, and pasting it again updates them.

### What do I do when git says my changes would be overwritten?

You changed a file that the update also changes. Follow [Keep your changes and still update](github.md#keep-your-changes-and-still-update).

### What's a merge conflict, and how do I fix it?

You and the project changed the same lines, and git wants you to choose. Follow [Part 9 of github.md](github.md#part-9-merge-conflicts).

### What's the difference between git-save and git-sync?

`git-save` sends your work to GitHub. `git-sync` does that too, and also brings in everyone else's work. See [git-save or git-sync?](github.md#git-save-or-git-sync).

### Why does vars.tin always show as changed?

The game keeps rewriting it. The helpers leave it out of commits, so that's normal.

### `git-sync: command not found`

The helpers aren't installed, or this terminal hasn't loaded them:

```bash
source ~/.bashrc
```

If that doesn't help, [install them](github.md#part-5-install-the-git-helpers).

### `fatal: Need to specify how to reconcile divergent branches`

You have your own commits, and the project has new ones too:

```bash
git pull --no-rebase --no-edit
```

### `Author identity unknown`

Tell git your name and email, then run your command again:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### `Permission to jmitchell33/3kdb.git denied`

You're on a plain clone, so you can't push to the main project. [Switch to a fork](github.md#part-4-switch-an-existing-clone-to-a-fork).

### Git asks for a username and password

Log in with the GitHub tool, and answer **Yes** to "authenticate Git":

```bash
gh auth login
```

### `fatal: destination path '3kdb' already exists`

You've already downloaded it, so update it instead.

### More git problems

See [Part 11 of github.md](github.md#part-11-problems-and-fixes).

[Back to top](#3kdb-faq)

---

## Errors and problems

### `tt++: command not found`

TinTin++ isn't installed, or it didn't finish installing. See [setup.md Step 1](setup.md#step-1-install-tintin-and-git).

### `#NO SESSION ACTIVE`

You typed a game command while not connected. If you're at the plain TinTin++ screen, type `#end`, then start from your `3kdb` folder.

### `#ERROR: #LINE LOG {logs/...}: COULDN'T OPEN FILE`

Your log folder is missing. Opening the menu creates it. If you logged in another way, run:

```bash
cd ~/3kdb
mkdir -p "logs/$(whoami)" vars
```

### `There is no reason to '...' here`

That's the game saying it doesn't know that command. Either 3kdb doesn't have an alias by that name for your guild, or it hasn't loaded. Check the spelling, or look it up with `dblib`.

### The screen looks broken or squashed

Make your terminal window bigger, or redraw it:

```text
init_screen
```

### I see `$eternal_string` on the screen

That spot on the data panel is for Eternal information, which needs level 111. Below that, it shows this raw name instead. It's harmless and doesn't affect anything.

### `Permission denied` when saving files

Something was probably run with `sudo`, which made those files belong to the admin account. To fix it:

```bash
sudo chown -R "$(whoami):" ~/3kdb
```

You don't need `sudo` for files inside `3kdb`, including with `nano`.

### Where do I get more help?

- Run `help` in the game for game questions.
- Use the 3kdb Discord channel, or ask Byron in the game.
- Run `dbinfo <command>` to see which file a command is in.

[Back to top](#3kdb-faq)
