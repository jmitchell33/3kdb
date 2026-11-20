# 3kdb FAQ

Short answers to common questions and problems. For the full explanation of how things work, see the [manual](manual.md).

Anything in a grey box is something to type or paste. `byron` is an example, so use your own character's name.

**Other guides:** [manual.md](manual.md), [setup.md](setup.md), [github.md](github.md), [tmux.md](tmux.md)

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
  - [Can I try the game without making a character?](#can-i-try-the-game-without-making-a-character)
  - [Some of my characters aren't showing on the menu](#some-of-my-characters-arent-showing-on-the-menu)
  - [My new character disappeared](#my-new-character-disappeared)
  - [It asks "Are you the owner of that character"](#it-asks-are-you-the-owner-of-that-character)
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
  - [How do I see what's changed in 3kdb?](#how-do-i-see-whats-changed-in-3kdb)
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
  - [How do I choose what happens after a kill?](#how-do-i-choose-what-happens-after-a-kill)
  - [The bot walks past mobs without fighting them](#the-bot-walks-past-mobs-without-fighting-them)
  - [Can I run several bots in a row?](#can-i-run-several-bots-in-a-row)
  - [How do I bot the Chaos Sewers?](#how-do-i-bot-the-chaos-sewers)
  - [The Section Z bot says I'm out of continues](#the-section-z-bot-says-im-out-of-continues)
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
- [Playing on a server (tmux)](#playing-on-a-server-tmux)
  - [What is tmux, and do I need it?](#what-is-tmux-and-do-i-need-it)
  - [How do I start 3kdb in tmux?](#how-do-i-start-3kdb-in-tmux)
  - [How do I leave it running and come back?](#how-do-i-leave-it-running-and-come-back)
  - [How do I switch from my PC to my phone?](#how-do-i-switch-from-my-pc-to-my-phone)
  - [My PC screen went small after I used my phone](#my-pc-screen-went-small-after-i-used-my-phone)
  - [My other device says detached, or joining seems to hang](#my-other-device-says-detached-or-joining-seems-to-hang)
  - [Can I scroll back in tmux?](#can-i-scroll-back-in-tmux)
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
  - [Something's broken that works for everyone else](#somethings-broken-that-works-for-everyone-else)
  - [How do I update TinTin++?](#how-do-i-update-tintin)
  - [tt++: command not found](#tt-command-not-found)
  - [#NO SESSION ACTIVE](#no-session-active)
  - [#ERROR: #LINE LOG {logs/...}: COULDN'T OPEN FILE](#error-line-log-logs-couldnt-open-file)
  - [There is no reason to '...' here](#there-is-no-reason-to--here)
  - [The screen looks broken or squashed](#the-screen-looks-broken-or-squashed)
  - [I see $eternal_string on the screen](#i-see-eternal_string-on-the-screen)
  - [Permission denied when saving files](#permission-denied-when-saving-files)
- [dblog problems](#dblog-problems)
  - [dblog couldn't get the list of changes](#dblog-couldnt-get-the-list-of-changes)
  - [dblog says the list is saved, from github.com's feed, or from git history](#dblog-says-the-list-is-saved-from-githubcoms-feed-or-from-git-history)
  - [dblog can't save its files](#dblog-cant-save-its-files)
  - [GitHub didn't answer in time](#github-didnt-answer-in-time)
  - [dblog new says to download 3kdb again](#dblog-new-says-to-download-3kdb-again)
  - [Does dblog need Python or git?](#does-dblog-need-python-or-git)
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

No. That version is very far behind. Use https://tintin.mudhalla.net/install.php instead. If you already did, see [How do I update TinTin++?](#how-do-i-update-tintin)

### Does it work on Windows?

Yes, through Ubuntu, a Linux terminal that runs inside Windows. [setup.md Step 1](setup.md#step-1-install-tintin-and-git) shows how to install it.

### Can I play on a phone?

3kdb has a phone layout, which switches on when your terminal is 75 columns wide or less. You still need a terminal on your phone that's connected to a machine with 3kdb installed. To carry on a game you started on your PC, use tmux. See [How do I switch from my PC to my phone?](#how-do-i-switch-from-my-pc-to-my-phone)

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

Your password won't be sent upstream. Git ignores `private.tin`, so it stays on your computer, and the game's saved settings in `vars.tin` don't include it.

### Does Remove delete my character?

No. It only takes the character off the menu, and the files stay. Your game character isn't affected either.

### Can I try the game without making a character?

Yes. Pick `[ Log in as guest ]` on the menu. It needs no password, and the game doesn't save guests.

### Some of my characters aren't showing on the menu

They're further down the list. It shows as many as fit on your screen and scrolls as you move. `▲ 3 above   ▼ 5 below` under it shows how many are hidden. Use the arrow keys or Page Up and Page Down, or tap that row.

### My new character disappeared

The game warns that level 1 characters aren't saved when you quit, and `help purge` says one that doesn't log in for 2 weeks is purged. Getting to level 2 only takes 300 more experience, from killing a few monsters. If it's gone, log in from the menu and it asks to create the name again.

### It asks "Are you the owner of that character"

That name is in use by a character that isn't saved yet, like a new level 1 still logged in somewhere. If it's yours, type `y`. Your saved password is used for you, or type it if you didn't save one, then answer the new character questions again. The old copy gets disconnected. If it isn't yours, type `n` and pick another name.

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

### How do I see what's changed in 3kdb?

Type `dblog`. It shows the 10 newest changes, with a `*` on ones you haven't seen yet, and 3kdb tells you at login when new ones have come in. `dblog more` shows the next 10 and `dblog all` shows them all.

```text
dblog hell bot
dblog file westersea
dblog show 558f098
```

Add words to search, or use `file`, `by <name>` or `since 2w`. `show` gives the full write-up of one change. `dblog new` checks GitHub for changes you haven't pulled yet, and `dblog help` lists everything. See [Finding commands](manual.md#finding-commands).

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

In Rastafan Hell's Swirling Mists, these need this week's exit words first. Walk a few steps with `hnext`, then try again.

### How do I log out?

Use `ld` to stay linkdead. Your character stays in the game and keeps its equipment. `quit` logs out fully, and you can lose equipment. See [Leaving the game](manual.md#leaving-the-game).

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

It's waiting at a long help page. Press Enter for the next page, or `q` to stop. To stop the pauses, run `setmod ROWS 999`. See `help setmod` for more.

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

`toggle-list` shows them all, and `toggle <name>` flips one. `toggle-list <word>` finds one, and `toggle-reset` puts them all back to how they started, after asking first.

### How do I stop xp and coins showing after every kill?

Type `toggle kill_stats`. 3kdb stops checking `xp`, `coins` and `(cstats` after kills. Kills still count, but xp and coins earned show 0 in the XP tracker, bot stats and `3kReport`. Mages still check `coins` for their familiar. Type it again to turn them back on.

### How do I change guild?

Use `gswap <guild>` as usual, and 3kdb follows. You need the perk for it in the game.

### Where are my chat logs?

In `logs/<your system username>/chatlogs/`, inside your `3kdb` folder, one file per day. Older ones may be compressed (`.zst`): read those with `zstdless`.

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

### How do I get through Rastafan Hell?

Its exits change every Wednesday, so there's no fixed path. `+hell` runs the stepper from outside, and `hnext` takes one step at a time. `hell-help` lists everything. See [Rastafan Hell](manual.md#rastafan-hell).

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

### How do I choose what happens after a kill?

Corpse actions run after each kill, such as wrapping the corpse, picking up loot or bagging it. `corpsetrig-all` shows your list and every action you can add, and `corpsetrig+ <name>` adds one. See [Corpse actions](manual.md#corpse-actions).

### The bot walks past mobs without fighting them

There are a few reasons. The mob may not be on that bot's target list, or your map may not match where you are (run `findhere`). On a laggy connection the bot can also move on before the game has caught up after a kill. If lag is the cause, add a delay to your corpse actions, such as `corpsetrig+ delay` (2 seconds), `delay5` or `delay10`. See [Corpse actions](manual.md#corpse-actions).

### Can I run several bots in a row?

Yes, with the bot cycler. See [Run several areas in a row](manual.md#run-several-areas-in-a-row).

### How do I bot the Chaos Sewers?

The map can't walk into the sewers, so `+sewers` takes you in through the bowl first, works out where you landed, walks to the start room and starts. It works from anywhere, and in the bot cycler. `sewers-in` does the same without starting the bot.

### The Section Z bot says I'm out of continues

`+sectionz-20` and `+sectionz-40` start with a continue code, and each new run uses one continue. `tagcheck` shows how many you have left. With none left the bot stops, or the cycler moves on to the next area. `+sectionz`, `+sectionz-fast` and `+sectionz-arcade` don't need continues. If a run stops partway, start the same bot again: it carries on from the room you're in, or unpauses back to where you last paused (even after a disconnect), without using a continue. It only uses one when you're somewhere off its path.

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

The game only sees your change after you load it:

```text
.reload
```

Or load just the file you changed:

```text
#read chars/byron/aliases.tin
```

If it still doesn't work, look for a missing `;` or `}`. See [If something doesn't work](manual.md#if-something-doesnt-work).

### My action doesn't fire

Check the pattern matches the game's text exactly. Only one action fires per line of text, so 3kdb may have one on that line already. A priority can put yours first. See [Be careful with actions](manual.md#be-careful-with-actions).

### My action keeps firing forever

It's setting itself off. Type this and press Enter to remove all your actions, then fix the file and run `.reload` or `#read chars/byron/actions.tin`:

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

## Playing on a server (tmux)

### What is tmux, and do I need it?

tmux holds your terminal for you. 3kdb runs inside it, so it keeps running and stays connected to the game when you close the window or your connection drops. You can then pick it up again from the same device or another one.

It's optional. It's worth it if 3kdb runs on a server you SSH into, or if you want to switch between your PC and your phone. If you only play in a terminal on your own PC, you don't need it. [tmux.md](tmux.md) has the full guide.

### How do I start 3kdb in tmux?

Install it once on the machine that runs 3kdb, then start or rejoin the session named `3k`:

```bash
sudo apt install -y tmux
```

```bash
tmux new -A -s 3k
```

The first time, start 3kdb inside it with `cd ~/3kdb` and `tt++ startmenu.tin`. The same `tmux new -A -s 3k` starts the session if it isn't running, or joins it if it is. See [Settings for 3kdb](tmux.md#settings-for-3kdb) for the one setting worth adding.

### How do I leave it running and come back?

Press `Ctrl+b`, let go, then press `d`. Closing the window, or losing your connection, does the same. 3kdb keeps running and your character stays logged in, not linkdead. To come back, SSH in and run `tmux new -A -s 3k` again.

To stop for good, use `ld` or `quit` in the game, close 3kdb, then type `exit`. See [Stop playing for good](tmux.md#stop-playing-for-good).

### How do I switch from my PC to my phone?

SSH into the same machine from your phone, with an app such as Termius, and run `tmux new -A -s 3k`. You're in the same game. 3kdb redraws for the phone's size about 3 seconds later.

Back on the PC, run the same command, or click in the PC window if it's still open. Then type a letter and delete it with Backspace. The screen grows back to PC size. Don't press Enter on an empty line, as that repeats your last command. See [Switch from your PC to your phone and back](tmux.md#switch-from-your-pc-to-your-phone-and-back).

### My PC screen went small after I used my phone

When two devices are attached, tmux sizes the game to the one you typed on last. Type a letter and Backspace on the PC to put it back in charge.

If it stays small, your tmux is older than 3.1, which always uses the smallest device, or your phone is still attached while asleep. Take the phone off by joining with this:

```bash
tmux new -A -D -s 3k
```

Or press `Ctrl+b` then `D` (Shift+d), pick the phone and press Enter. Adding `set -g window-size latest` to `~/.tmux.conf` stops it happening again. See [Why the screen changes size](tmux.md#why-the-screen-changes-size).

### My other device says detached, or joining seems to hang

`-D`, and `tmux attach -d`, take every other device off. The other device shows `[detached (from session 3k)]` and goes back to its prompt, or its SSH app closes. That's expected, and the game keeps running. Leave out `-D` to share the game between both devices instead.

If a device looks frozen, its own connection has died, for example a phone that went to sleep. Its screen stays stuck until its SSH app notices, but tmux and the game aren't waiting on it. Close that old screen or reconnect it. See [Take another device off](tmux.md#take-another-device-off).

### Can I scroll back in tmux?

Yes. Use 3kdb's **Page Up** and **Page Down** as normal. tmux's own scroll mode (`Ctrl+b` then `[`) doesn't hold 3kdb's scrollback properly. If you end up in it, press `q`.

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

Then run `.reload`, or log back in. If only one file changed, you can `#read` that file instead.

`dblog new` shows what an update would bring in before you pull, and `dblog` shows what's changed lately.

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

That's where your character's settings are saved, and the game keeps rewriting it. If your character is in the project, the file shows as changed soon after each commit. That's normal.

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

### Something's broken that works for everyone else

The most common cause is an old TinTin++. Check your version:

```bash
tt++ -V
```

3kdb is tested on **2.02.61**. Anything older, especially the 2.02.20 that `apt-get` installs, can show errors, draw the screen wrong, or quietly skip some 3kdb code. [Update TinTin++](#how-do-i-update-tintin) and try again before anything else.

### How do I update TinTin++?

Log out of the game and close tt++ first. Then install the latest version from the website, the same way as a first install:

https://tintin.mudhalla.net/install.php

Check it worked:

```bash
tt++ -V
```

If it still shows the old number, you have the old `apt-get` copy too, and it's being used instead. Remove it, then check again:

```bash
sudo apt remove -y tintin++
hash -r
tt++ -V
```

Your 3kdb folder and characters aren't touched by updating TinTin++.

### `tt++: command not found`

TinTin++ isn't installed, or it didn't finish installing. See [setup.md Step 1](setup.md#step-1-install-tintin-and-git).

### `#NO SESSION ACTIVE`

You typed a game command while not connected. If you're at the plain TinTin++ screen, type `#end`, then start from your `3kdb` folder.

### `#ERROR: #LINE LOG {logs/...}: COULDN'T OPEN FILE`

Your log folder is missing. Opening the menu creates it. If you logged in another way, run:

```bash
cd ~/3kdb
mkdir -p "logs/$(whoami)/chatlogs" "logs/$(whoami)/discord" vars
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

---

## dblog problems

### dblog couldn't get the list of changes

dblog asks GitHub for the list, and the rest of the message says why it couldn't. Most of them are about the internet connection, not 3kdb:

| The message says | What to do |
|---|---|
| curl isn't installed | `sudo apt install curl` |
| can't look up, or has no route to the internet | Your internet connection is down, or DNS isn't working. Check you can open a website. |
| was refused, or didn't answer within 10 seconds | A firewall is probably blocking GitHub. On a work or school network, ask whoever runs it. |
| was too slow, or was cut off before it answered | The connection is struggling. Try again in a few minutes. |
| The proxy in your https_proxy setting isn't working | Fix or remove the `https_proxy` setting in your terminal. |
| This computer's clock says | Set your computer's clock to the right date and time. |
| The secure connection failed | Something on your network, such as antivirus or a work firewall, is getting in the way. Try another network. |
| Something on the network answered instead | Usually a Wi-Fi login page. Open a website in your browser and log in to the Wi-Fi. |
| GitHub's API allows 60 requests an hour | Everyone on your internet address shares that limit. Wait until the time it gives. |
| GitHub is having problems right now | Try again later. |
| the repository doesn't exist or isn't public | The project has moved. Ask in the 3kdb Discord channel. |

dblog only asks GitHub every 10 minutes at most, so it won't use the hourly limit up by itself.

### dblog says the list is saved, from github.com's feed, or from git history

GitHub couldn't be reached, so dblog showed the best list it had instead, and says why on the same line. The saved list is from the last time it worked. github.com's feed only has the newest 20 changes. Your git history is missing anything since your last `git pull`. When GitHub can be reached again, the next `dblog` gets the full list.

### dblog can't save its files

The message names the file or folder, and the command that fixes it. Quit tt++ and run that command. It usually happens when tt++ or git was run with `sudo`, which made those files belong to the admin account. See [Permission denied when saving files](#permission-denied-when-saving-files).

### GitHub didn't answer in time

GitHub was slow. Type `dblog` again in a minute. You can keep playing while it fetches.

### dblog new says to download 3kdb again

Your 3kdb folder was downloaded or copied, not made with `git clone`, so `git pull` can't update it. dblog compared your files with GitHub's instead and lists the ones that are new or changed. To update, download 3kdb again and copy it over your folder. Your `chars` and `vars` folders aren't in the download, so they stay as they are. To make updating easier next time, see [How do I get updates?](#how-do-i-get-updates)

### Does dblog need Python or git?

No. It uses `curl`, which comes with Ubuntu. Without git, it still works, and `dblog new` compares your files with GitHub's instead.

[Back to top](#3kdb-faq)
