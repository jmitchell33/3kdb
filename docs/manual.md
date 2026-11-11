# 3kdb Manual

This is the full guide to 3kdb: what it is, how to use it, and how to add your own code. You don't need any coding experience. Read it from the top, or use the contents to jump to what you need.

**Other guides:**
- [setup.md](setup.md): the quick install steps
- [faq.md](faq.md): short answers to common questions and problems
- [github.md](github.md): updates, forks and sending in changes

**How to read this manual:**
- Anything in a grey box is something to type, paste or put in a file.
- Byron is the example player. Wherever you see `byron`, use your own character's name, in lower case.
- Words in angle brackets, like `<mob>`, mean "put your own word here". Leave out the `<` and `>`. So `kill <mob>` could become `kill rat`.

## Contents

- [What is 3kdb?](#what-is-3kdb)
  - [Words you'll see](#words-youll-see)
- [Installing 3kdb](#installing-3kdb)
- [Your first login](#your-first-login)
  - [Add your character](#add-your-character)
  - [Log in](#log-in)
  - [Run setup once](#run-setup-once)
  - [Try these first](#try-these-first)
- [The menu](#the-menu)
- [The screen](#the-screen)
- [Typing commands](#typing-commands)
- [Finding commands](#finding-commands)
- [Game rules you must know](#game-rules-you-must-know)
- [Getting around](#getting-around)
  - [Make sure the map knows where you are](#make-sure-the-map-knows-where-you-are)
  - [Walk to a place](#walk-to-a-place)
  - [Search the map](#search-the-map)
  - [Update the map](#update-the-map)
- [Bots](#bots)
  - [Start a bot](#start-a-bot)
  - [Control a running bot](#control-a-running-bot)
  - [Check on a bot](#check-on-a-bot)
  - [Bot settings](#bot-settings)
  - [Run several areas in a row](#run-several-areas-in-a-row)
  - [Add your own steps](#add-your-own-steps)
  - [Rastafan Hell](#rastafan-hell)
- [Deadman timer](#deadman-timer)
- [Fighting](#fighting)
  - [Strategies](#strategies)
  - [Mob kill actions](#mob-kill-actions)
  - [Corpse actions](#corpse-actions)
- [Guilds](#guilds)
- [Trackers and reports](#trackers-and-reports)
- [Crafting and professions](#crafting-and-professions)
- [Chat, logs and Discord](#chat-logs-and-discord)
  - [Chat window](#chat-window)
  - [Logging everything](#logging-everything)
  - [Sending chat to Discord](#sending-chat-to-discord)
- [Settings](#settings)
  - [Toggles](#toggles)
  - [Hide spam (gags)](#hide-spam-gags)
  - [Colours](#colours)
  - [Data panel](#data-panel)
  - [Hide the map](#hide-the-map)
  - [Sounds](#sounds)
- [Leaving the game](#leaving-the-game)
- [Making your own commands](#making-your-own-commands)
  - [Where your code goes](#where-your-code-goes)
  - [Pick an editor](#pick-an-editor)
  - [Your first alias](#your-first-alias)
  - [Aliases with your own words](#aliases-with-your-own-words)
  - [Your first action](#your-first-action)
  - [Actions that catch words](#actions-that-catch-words)
  - [Be careful with actions](#be-careful-with-actions)
  - [Variables](#variables)
  - [Making decisions](#making-decisions)
  - [Colour, hide or change text](#colour-hide-or-change-text)
  - [Check something every round](#check-something-every-round)
  - [Bot hooks](#bot-hooks)
  - [The deadman alias](#the-deadman-alias)
  - [Load your changes](#load-your-changes)
  - [If something doesn't work](#if-something-doesnt-work)
  - [Saving your code](#saving-your-code)
- [Keeping 3kdb updated](#keeping-3kdb-updated)
- [Where everything lives](#where-everything-lives)
- [Command reference](#command-reference)
  - [General](#general)
  - [Mapping](#mapping)
  - [Bot commands](#bot-commands)
  - [Combat](#combat)
  - [Corpses](#corpses)
  - [Trackers](#trackers)
  - [Crafting](#crafting)
  - [Professions](#professions)
  - [Chat (MIP)](#chat-mip)
  - [Eternal](#eternal)
  - [ROLM](#rolm)
  - [Chaos areas](#chaos-areas)
  - [Fantasy areas](#fantasy-areas)
  - [Science areas](#science-areas)
  - [Debugging](#debugging)
  - [Guild commands](#guild-commands)

---

## What is 3kdb?

**3Kingdoms** (3k) is a MUD: an online game played entirely with text. You read what's happening and type what you want to do.

**TinTin++** (`tt++`) is the program that connects you to the game. It's called a MUD client. On its own, it just shows text and sends what you type.

**3kdb** is a big collection of TinTin++ scripts that sits on top. It adds:

- a screen with a map, chat window, health bars and stats
- a map of the game that can walk you to places
- bots that can run through areas for you while you watch
- trackers for damage, experience and items
- tools for every guild, and for crafting
- a place for your own custom commands

### Words you'll see

- **Alias:** a short command you make that runs other commands.
- **Action** (or trigger): something that runs by itself when certain text appears.
- **Bot:** a script that walks an area and fights for you.
- **Speedrun:** a named place the map can walk you to, like `shop`.
- **Vnum:** a room's ID number on the map.
- **MIP:** the behind-the-scenes data feed 3kdb uses for your health bars and chat window.
- **Gag:** hiding lines of text you don't want to see.
- **Linkdead:** your character is still in the game, but you're disconnected.
- **Mob:** a monster or other creature in the game.
- **CoT:** Center of Town, the main hub of the game.
- **GXP:** guild experience.
- **VAF:** a game perk. Some 3kdb features need one, and the command list says when they do.
- **Repo:** short for repository. It's the `3kdb` folder and everything in it.

[Back to top](#3kdb-manual)

---

## Installing 3kdb

[setup.md](setup.md) has the full steps with fixes for common problems. The short version, once TinTin++ and git are installed:

```bash
cd ~
git clone https://github.com/jmitchell33/3kdb.git
cd 3kdb
tt++ startmenu.tin
```

Don't install TinTin++ with `apt-get`, because that version is very far behind. Use the instructions at https://tintin.mudhalla.net/install.php instead.

[Back to top](#3kdb-manual)

---

## Your first login

### Add your character

1. On the menu, press **Enter** on `[ Add ]`.
2. Type your character's name and press Enter.
3. Type your guild and press Enter. No guild yet? Type `adventurer`.
4. Type your password and press Enter, or just press Enter to type it at each login.

The menu creates everything your character needs.

### Log in

Press **Enter** on your character. You'll see the screen fill up as 3kdb loads. Give it about 10 seconds to finish.

If the name isn't on the game yet, it asks `Would you like to create this character`. Check the spelling, then type `y` to create it, or `n` to cancel. Your saved password is used for you, and the game asks a few more questions. See [Step 5 of the setup guide](setup.md#step-5-log-in). Get to level 2 soon, because level 1 characters can be lost. 3k also only allows one character per player until level 50, so read `help characters` before making a second one.

### Run setup once

Do this once per character. Type each line and press Enter:

```text
setup_3kdb
setup_3kdb_hpbar
```

`setup_3kdb` changes some game settings so that 3kdb can read rooms and monsters properly. `setup_3kdb_hpbar` sets up your guild's health bar. Not every guild has one, so if the game says `There is no reason to...`, skip it.

**Bards:** 3kdb assumes you also have this setting on:

```text
bset auto_shield 1
```

### Try these first

```text
dblib
speedruns
botlist
strategies
```

[Back to top](#3kdb-manual)

---

## The menu

The menu is what you see each time you start:

```bash
cd ~/3kdb
tt++ startmenu.tin
```

**On the character list:**
- **Up / Down:** pick a character
- **Left / Right:** change guild, if you listed more than one
- **Enter:** log in
- **1 to 9:** log in directly. With 10 or more characters, or if the list doesn't all fit on your screen, type the number and then press Enter.
- **Page Up / Page Down:** move a screenful, if the list doesn't all fit
- **Tab:** jump to the Edit and Remove buttons
- **q:** close the program

**On the button row:**
- **Add:** add a character
- **Edit:** change a character's guild list. The first one listed is the default.
- **Remove:** take a character off the menu. Its files are kept.
- **Log in as guest:** play straight away with no character or password. The game doesn't save guests.
- **Quit:** close the program

You can also click names, guild arrows and buttons. Hold **Shift** to select text while the menu is showing.

The list shows as many characters as your screen has room for and scrolls as you move. `▲ 3 above   ▼ 5 below` under it shows how many are hidden. You can tap or click that row to page through the list, or use the mouse wheel.

**The menu also shows:**
- **Next reboot:** when the game will next restart. It appears after a character has logged in.
- **Linkdead timers:** how long until the game boots a character you left linkdead.

**Refreshing linkdead timers:** press **0** twice quickly. The menu logs each linkdead character in and drops it again, which restarts its timer.

Typing anything else at the menu runs it as a TinTin++ command.

[Back to top](#3kdb-manual)

---

## The screen

Once you're logged in, the screen has these areas. Their exact size depends on your window.

- **Chat window (top left):** tells, party, clan, guild and high mortal chat, kept apart from the game text. The header shows `TELLS PARTY CLAN GUILD HM`.
- **Status bar (below chat):** idle time, the deadman countdown, game uptime, time to reboot, lag, and combat status.
- **Game text (middle left):** the main game output. This is where you read what's happening.
- **Map (top right):** where you are. It follows you as you walk.
- **Data panel (lower right):** tabs for **General**, **Bot** and **Map**. It shows corpses, bot status, the XP tracker and active strategies.
- **HP bars (bottom):** health, spell points, guild points and enemy health.
- **Input line (very bottom):** what you're typing.

**Useful commands:**
- `mapFull` switches the map to full screen. Run it again to switch back.
- `hidemap` hides the map and gives its space to the data panel. `showmap` brings it back. See [Hide the map](#hide-the-map).
- `caption_view general` or `caption_view bot` switches data panel tabs.
- `caption-help` explains the data panel.
- `init_screen` redraws the whole screen if it looks wrong.
- `draw_all` redraws the panels.

**On a small screen or phone:** 3kdb switches to a phone layout when the window is 75 columns wide or less. It redraws when you resize the window.

The start menu fits itself to your screen too. The logo shrinks to one line, and the character list scrolls, so the buttons always stay in view.

[Back to top](#3kdb-manual)

---

## Typing commands

**Run several commands at once** by putting `;` between them:

```text
say one;say two
```

**Press Enter on an empty line** to repeat your last command. This is handy in fights, but be careful with it.

**Up and Down arrows** go back through what you've typed.

**Page Up and Page Down** scroll back through the game text.

**Search what's on screen** with `grep`:

```text
grep hello
```

**Do maths** with `calc`:

```text
calc 100/5*25
```

**Walk with the keyboard** using Alt plus a letter:

- `Alt+i` north, `Alt+m` south, `Alt+j` west, `Alt+l` east
- `Alt+u` northwest, `Alt+o` northeast, `Alt+n` southwest, `Alt+,` southeast
- `Alt+k` look

**Use the mouse** with `qq`. It turns mouse clicks on or off, so you can click the data panel tabs. Run `qq` again to turn it off, which also lets you select text normally.

**Long help pages** stop with `More: 0-19(26) : [q,b,<cr>]`. Press Enter for the next page, `b` to go back, or `q` to stop. To stop the pauses, set a bigger page size. `help setmod` explains this and the other options:

```text
setmod ROWS 999
```

**Commands starting with `#`** go to TinTin++ itself, not the game. TinTin++ has its own help too:

```text
#help alias
```

[Back to top](#3kdb-manual)

---

## Finding commands

3kdb has hundreds of commands, so you won't remember them all. These find them for you.

**List commands by type:**

```text
dblib bot
```

The types are `eternal`, `rolm`, `crafting`, `mapping`, `chaos`, `fantasy`, `science`, `guild`, `misc`, `corpse`, `combat`, `profession`, `debug`, `trackers`, `bot` and `mip`.

**List your guild's commands** using 3 or more letters of its name:

```text
dblib bard
```

**List commands starting with some letters:**

```text
dblib map
```

**Get details on one command:**

```text
dbinfo go
```

That shows its type, how to use it, what it does, and which file it's in.

**The game has its own help** too:

```text
help
```

The [command reference](#command-reference) at the end of this manual lists 3kdb's commands in one place.

[Back to top](#3kdb-manual)

---

## Game rules you must know

3k has rules about scripts and bots, and 3kdb makes it easy to break them by accident. Read them yourself:

```text
help rules
```

In short, as those rules say:

- **Be present when you play.** Most scripting is allowed, but you must be able to answer players and wizards within a reasonable time while you're advancing your character. Leaving automation running while you're away is not allowed. Just hanging out doing nothing is fine.
- **Don't get in other players' way.** If your script steals a kill, corpse or equipment, stop, sort it out with them, and fix your script.
- **No anti-idling.** You must never have a trigger or timer that just keeps you from going idle.
- **Extra characters have rules too.** The menu makes it easy to have many characters, so read this as well:
  ```text
  help seconds
  ```

If you're not sure whether something is allowed, ask a wizard before you do it. The rules in the game always win over anything in this manual.

[Back to top](#3kdb-manual)

---

## Getting around

### Make sure the map knows where you are

The map has to match where you really are, or walking commands will go wrong. If it looks wrong:

```text
findhere
```

When it works, it says `YOU HAVE BEEN FOUND`. If several rooms look the same, these walk around until it knows for sure:

```text
findhere-auto
```

```text
findhere-auto stop
```

To set the map position yourself, without moving your character:

```text
mapgo cot
```

### Walk to a place

See where you can go:

```text
speedruns
```

The list is long, so you can filter it by `shop`, `mob`, `area`, `eq`, `misc`, `clan` or `crafting`:

```text
speedruns shop
```

Walk there:

```text
go shop
```

Walk back to where you ran `go` from:

```text
go_back
```

If a bot is running, `go` pauses it first.

### Search the map

- `mapfind <text>` lists rooms matching your text.
- `mapsearch <text>` searches room names and notes.
- `mappath <text>` finds a path to a matching room and shows it.

### Update the map

You only need these if you're adding to the map. `maphelp` lists them all.

- `mapon` / `mapoff` turns live mapping on or off.
- `mapexplore <area>` walks and maps every unvisited room in an area. `mapexplore stop` stops it.
- `mapname <name>` renames this room.
- `mapnote <note>` adds a note to this room.
- `maplm <label>` makes a landmark label for this room.
- `mapUndo` undoes your last map edit.
- `mapbackup` saves a dated backup of the map.
- `mapsave` / `mapload` saves or loads the shared map file.

The map file is part of the project, so saving changes to it can cause a [merge conflict](github.md#part-9-merge-conflicts) when you update. Make a backup first.

[Back to top](#3kdb-manual)

---

## Bots

A bot walks an area and fights for you. **You must stay at your computer and pay attention while it runs.** See [Game rules you must know](#game-rules-you-must-know).

### Start a bot

See all of them:

```text
botlist
```

Before you start, check your map is right with `findhere`. Some bots are much too dangerous for new characters. Read the area's name, and check you're strong enough for it.

**Walk to the start and begin automatically** with `+` and the bot's name:

```text
+turkeys
```

**Check first and ask** with `-` and the bot's name:

```text
-turkeys
```

If you're not in the right room, you get three choices for 5 seconds:

- **1:** you're in the wrong room, so run there
- **2:** you're in the right room, but the map needs moving
- **3:** run the bot anyway

### Control a running bot

- `.pause` pauses it.
- `.unpause` unpauses it.
- `.resume` returns to the room where you paused, then carries on after 10 seconds.
- `..` tells it to walk, if it has stopped and you don't know why.
- `.skip` leaves this room's mob alone and moves on.
- `.stop` stops and ends the bot.

### Check on a bot

- `bot_report` shows progress and what it has picked up.
- `3kdb` shares the bot's status on party chat.
- `caption_view bot` shows the bot tab on the data panel.

### Bot settings

- `playercheck` turns the check for other players on or off.
- `autocollect` turns picking up all items on or off.
- `whitelist` shows your VIP list, the players `playercheck` ignores. `whitelist+ <name>` adds one, `whitelist- <name>` removes one, and `whitelist-party` adds your party.

### Run several areas in a row

This is the bot cycler:

- `bcy+ <bot>` adds a bot to the list, such as `bcy+ smurfs`.
- `bcy- <bot>` removes one.
- `bcy` shows the list.
- `botclear` clears it.
- `nextarea` starts the next area.

### Add your own steps

The easiest way is [mob kill actions](#mob-kill-actions), a list of commands that fire when you start a fight, including when a bot starts one. Use `mka+` to add one.

For anything else, your character's `config.tin` can run commands before a bot starts or before each fight. See [Bot hooks](#bot-hooks).

### Rastafan Hell

Hell's Swirling Mists, through the Portal of Evil, is a stack of dark rooms whose exits are words like `yonder` and `thisway`. The words point a different way every Wednesday, by the mud's clock (`time`). 3kdb works them out as you walk, and saves them in `vars/boot.tin` so all your characters can use them.

- `+hell` starts the stepper from outside. It walks in, fights every devil on planes 1 to 4, then walks plane 5 to the mountain room and stops. `hellbot` starts it from inside the mists.
- `hnext` takes one step toward the mountain, if you'd rather walk yourself.
- Inside the mists, `n`, `e`, `s`, `w`, `u` and `d` move by this week's words. `u`, `n` and `e` head down toward the mountain.
- `hell` shows the plane you're on and this week's words, and `hell-help` lists every command.
- The map follows you, and `findhere` and `findhere-auto` work there once the week's words are known.

Past the sign room on plane 4, monsters won't let you leave a fight. You can't quit, teleport or run. In the mountain room, type `scale mountain` to climb.

[Back to top](#3kdb-manual)

---

## Deadman timer

The deadman is your safety switch. **It's 15 minutes by default.** If you don't type anything for that long, it pauses your bot and runs any actions you've set up. Typing anything resets the countdown. You can see the time left on the status bar.

Keep it at 15 minutes while you run bots, so that a bot can't carry on for long if you've walked away. Don't try to get around it. See [Game rules you must know](#game-rules-you-must-know).

**Commands:**

- `deadman` shows the full help.
- `deadman <minutes>` sets the timer. To put it back to the default:
  ```text
  deadman 15
  ```
- `deadman-list` shows the extra actions you can add.
- `deadman+ <name>` adds an action, such as `deadman+ ping`.
- `deadman- <name>` removes an action.
- `deadman-clear` removes them all.

To run your own commands when it fires, see [The deadman alias](#the-deadman-alias).

[Back to top](#3kdb-manual)

---

## Fighting

### Strategies

Strategies are guild attacks and tricks that 3kdb uses for you in combat. What's available depends on your guild.

- `strategies` shows which are active and which aren't.
- `strategy-list` lists them with descriptions.
- `strategy <name>` turns one on or off.
- `strategy-clear` turns them all off.

### Mob kill actions

These are commands to fire when you start a fight. `mka` runs your list, then attacks.

- `mka <mob>` runs your actions and attacks that mob. On its own, `mka` attacks the first mob it finds in the room.
- `mka-help` shows the help.
- `mka-all` shows the available actions.
- `mka-check` shows your current list.
- `mka+ <name>` adds an action, and `mka- <name>` removes one.
- `mka++ <name>` raises its priority, and `mka-- <name>` lowers it.
- `mka-on` / `mka-off` turns them on or off.
- `mka-clear` clears your list.

### Corpse actions

These run after a kill, such as looting or using the corpse. They have their own similar list.

- `corpsetrig-help` shows the help.
- `corpsetrig-all` shows your list and the available actions.
- `corpsetrig+ <name>` adds an action, and `corpsetrig- <name>` removes one.
- `corpsetrig++ <name>` raises its priority, and `corpsetrig-- <name>` lowers it.
- `corpsetrig-kb` switches between your killing blows only and all kills.
- `corpsetrig-on` / `corpsetrig-off` turns them on or off.
- `corpsetrig-clear` clears your list.

[Back to top](#3kdb-manual)

---

## Guilds

Each guild has its own commands, such as attacks, buffs and trackers. To see yours, use 3 or more letters of the guild's name:

```text
dblib bard
```

Guilds with health bars are set up by `setup_3kdb_hpbar`. Some guilds also have `maint`, which keeps chosen defenses up. Use `maint-help` to find out more.

**Changing guild:** swap in the game as normal, and 3kdb follows:

```text
gswap mage
```

It reloads its scripts once the game confirms, and remembers your guild for next login. You can only swap to a guild if you have the perk for it in the game. You can also pick a guild on the menu if you listed more than one.

**3kdb's guild folders:** adventurer, angel, bard, bladesinger, breed, changeling, cyborg, elemental, eternal, fremen, gentech, jedi, juggernaut, knight, knights-zorb, mage, monk, necromancer, priest, psicorps and sii.

**Eternal commands** are in their own group, so you can see them with `dblib eternal`.

[Back to top](#3kdb-manual)

---

## Trackers and reports

- `3kReport` is the kill report. `3kReport 10` shows your last 10 kills, and `3kReport <mob>` filters by mob. `3kReport-clear` clears it.
- `dstats` is the damage report, and `dreset` resets it. It needs the numbers perk.
- `defStats` is the defense report, and `defStats_reset` resets it.
- `istats` is the item tracker, and `istats_reset` resets it.
- `rounds` is the combat round tracker. Turn it on with `toggle rounds`. It shows your rounds all time, this session, and how many each guild level took. It reads your guild level from `score`, and `recover` checks `score` by itself, for any guild. `rounds note <text>` adds your own line to the log, `rounds check` reads `score` again, and `rounds-help` explains it all. 3kdb also reads `score` (hidden) at every login and return from linkdeath; typing `score` yourself always shows it. It keeps its own count, so nothing that clears `total_rounds` touches it. The count is saved every round to `logs/<your system username>/rounds/`, so a crash or linkdeath loses at most one round.
- `reset_xp` resets the XP tracker on the data panel.
- `reset_gxp` resets guild experience tracking.
- `.reps` is the reputation tracker.

Some guilds have more. Check `dblib trackers` and `dblib <your guild>`. For example, necromancers can turn on `toggle circle_tracker` to add their Next Circle progress to the health bar, and `circle_tracker` shows a table of guild experience by Comtrance mode and power.

[Back to top](#3kdb-manual)

---

## Crafting and professions

`dblib crafting` and `dblib profession` list everything. The main ones are:

- **Mining:** `miner-on`, `mine-list`, `mine <deposit>`, `minefor-list`, `minefor <jewel>`, `miner-off`
- **Smelting:** `smelter-on`, then `autosmelt <preset>`
- **Blacksmithing:** `forge-on`, `forge-off`, `killforge`
- **Farming:** `farmer-on`, `farmer-off`
- **Gems and jewels:** `gem-lookup help`, `jewel-lookup help`, `make-gem help`
- **Mining deposits:** `deposit-lookup help`
- **Assembling:** `assembler`, `stashlist assemble`
- **Transmuting:** `transmute_ratios`, `transmuter-stats`, `transmute_burn`
- **Reforging:** `ref <item> <ACtype>`, `refg <item> <ACtype>`

3kdb reads your profession at login and loads the matching scripts.

[Back to top](#3kdb-manual)

---

## Chat, logs and Discord

### Chat window

Tells, party, clan, guild and high mortal chat all show in the chat window. They're also saved to `logs/<your system username>/chatlogs/`, one file per day.

To hide someone from the chat window:

- `blacklist` shows your list.
- `blacklist+ <name>` adds someone.
- `blacklist- <name>` removes someone.
- `blacklist-clear` empties the list.

Blacklisted messages are still logged, and still go to Discord if you've set that up.

`th` shows your tell history.

### Logging everything

```text
toggle sessionlog
```

This saves everything you see to `logs/<your system username>/sessions/`, one file per day, and stays on for this character. `sessionlog on` and `sessionlog off` start or stop it for now. Old days are compressed if you have `zstd` installed. Read those with `zstdless` or `zstdgrep`.

### Sending chat to Discord

This posts your chat into your own Discord server.

**1. Make a webhook in Discord.** In your server, go to **Server Settings**, then **Apps**, **Integrations**, **View Webhooks**, **New Webhook**. Name it, pick a channel, and copy its URL. **Treat this URL like a password**, because anyone who has it can post to your channel.

**2. Install what the script needs.** On Ubuntu:

```bash
sudo apt update
sudo apt install -y python3 python3-requests
```

**3. Add the URL to your character's private file:**

```bash
nano ~/3kdb/chars/byron/private.tin
```

Find the lines for the channels you want, and remove the `#NOP -- ` from the front. Replace the example URL with yours. For example:

```text
#var webhook[url][general] https://discord.com/api/webhooks/long_token;
```

Every post goes to `general`, and also to its own channel when that one is set. Save with `Ctrl+O`, Enter, then `Ctrl+X`.

**4. Turn it on in the game:**

```text
#read chars/byron/private.tin
toggle discord_post
```

`.reload` works too, in place of the `#read`.

If posts don't appear, look for errors in `logs/<your system username>/discord/discordPost.log`.

`private.tin` is never uploaded by git, so your URLs stay private as long as you keep them in that file.

[Back to top](#3kdb-manual)

---

## Settings

### Toggles

Toggles turn small features on or off. They're saved for each character.

```text
toggle-list
```

That shows them all, whether each is on, and what it does. To flip one:

```text
toggle mission
```

To find one, add a word. It matches part of a name or description, and `on` or `off` lists by status:

```text
toggle-list notify
```

To put every toggle back to how it started, use `toggle-reset`. It lists what would change first, and nothing happens unless you type this within 30 seconds:

```text
toggle-reset confirm
```

### Hide spam (gags)

```text
gags
```

That lists the groups you can hide, such as combat spam and blank lines.

- `gag+ <group>` hides a group.
- `gag- <group>` shows it again.
- `gag-all` hides them all.
- `gag-clear` shows them all.

### Colours

- `themes` lists the colour themes.
- `themes <name>` previews one.
- `theme <name>` switches to it, such as `theme bright`. You may need to run `ld` and log back in to see all of it.
- `colors` shows the available colours.

### Data panel

- `caption-help` explains the panel.
- `caption` shows the panel's items.
- `caption+` adds an item, and `caption-` removes one.

### Hide the map

The map shows by default. If you'd rather have more room for the data panel:

```text
hidemap
```

The panel moves up to fill the space. Only the picture of the map goes away, so `go`, `findhere` and bots all still work. The room name and notes strip goes too, because it sits inside the map.

Your choice is saved for each character, so it stays hidden until you bring it back:

```text
showmap
```

`toggle hidemap` does the same thing, and `toggle-reset` shows the map again. `mapFull` still opens the full screen map while it's hidden.

### Sounds

- `beepon` / `beepoff` turns the terminal beep on or off.

[Back to top](#3kdb-manual)

---

## Leaving the game

There are two ways to leave, and they aren't the same. Use `ld` unless you mean to log out fully.

**`ld`** saves your settings and disconnects, leaving your character linkdead in the game with its equipment. You go back to the menu, which shows a timer.

```text
ld
```

Without the linkdead perk, the game boots a linkdead character after 24 hours. With it, only a reboot does.

**`quit`** logs your character out fully, and you can lose equipment. You go back to the menu.

```text
quit
```

To close the program from the menu, press `q`. In plain TinTin++, type `#end`.

[Back to top](#3kdb-manual)

---

## Making your own commands

This is where 3kdb becomes yours. You can add commands and automatic responses to your character without touching anyone else's code.

### Where your code goes

Every character has its own folder at `chars/byron/`. These are the files you'll use:

- **`aliases.tin`:** your own commands
- **`actions.tin`:** things that run when certain text appears
- **`config.tin`:** steps to run before bots and fights
- **`heartbeat.tin`:** things to check every round
- **`tickers.tin`:** things to run on a timer
- **`miphp.tin`:** your own custom health bar
- **`private.tin`:** passwords, webhook URLs and secrets, never uploaded by git

3kdb loads these for you at each login. **Keep your own code in these files** rather than changing `common/` or `modules/`. Then updates are far less likely to clash with your changes.

**Leave these alone:**
- `vars.tin`, because the game rewrites it all the time
- `guild.tin`, because the menu and `gswap` write it

### Pick an editor

An editor is a program for changing text files. Any of these will work, so use whichever you like.

**nano** is already in your terminal, and it's the simplest to start with:

```bash
nano ~/3kdb/chars/byron/aliases.tin
```

Use the arrow keys to move. Press `Ctrl+O` then Enter to save, and `Ctrl+X` to exit.

**VS Code** is free from https://code.visualstudio.com. It's the most popular choice if you plan to do a lot of editing. To open the whole folder:

```bash
cd ~/3kdb
code .
```

On Windows, also install its **WSL** extension. VS Code has no TinTin++ colouring built in, but setting the language to C++ works decently.

**Notepad++** is a free Windows editor from https://notepad-plus-plus.org. To reach your files from Windows, run this and open the `chars` folder in the window that appears:

```bash
cd ~/3kdb
explorer.exe .
```

**Windows Notepad** works too:

```bash
cd ~/3kdb/chars/byron
notepad.exe aliases.tin
```

**On Windows**, keep your files inside Ubuntu, in `~/3kdb`, and not in a Windows folder.

### Your first alias

An alias is a short command you make up. Let's make `hi` say hello.

**1. Open your aliases file:**

```bash
nano ~/3kdb/chars/byron/aliases.tin
```

**2. You'll see this.** Your code goes between the two `#class` lines, in the gap:

```text
#class {player_aliases} {kill}
#class {player_aliases} {open}

#NOP -- Player specific aliases;

#class {player_aliases} {close}
```

**3. Add your alias in the gap:**

```text
#alias {hi}
{
    say hello everyone;
};
```

**4. Save the file.** In nano, press `Ctrl+O`, Enter, then `Ctrl+X`.

**5. Load it in the game:**

```text
.reload
```

For a small change like this, you can load just this file instead with `#read chars/byron/aliases.tin`.

**6. Try it:**

```text
hi
```

You should see `You say: hello everyone`. That's your first alias.

**Why the file has those `#class` lines:** they group your aliases together. When the file loads, `kill` removes the old copies, `open` starts the group, and `close` ends it. Keep your code between `open` and `close`.

**Every command ends with `;`.** Forgetting it is the most common mistake.

### Aliases with your own words

`%1` means "the first word typed after the alias", `%2` the second, and so on. `%0` means all of them.

```text
#alias {greet}
{
    say hi there %1;
};
```

Now `greet bob` makes you say `hi there bob`.

**Several commands** just go on separate lines:

```text
#alias {prepare}
{
    look;
    inventory;
    score;
};
```

**Doing something later** uses `#delay`, with the number of seconds:

```text
#alias {getready}
{
    look;
    #delay {2}
    {
        say two seconds later;
    };
};
```

**Pick a name that isn't already used.** If yours matches a 3kdb alias, it replaces it. Run `dblib <name>` first to check.

### Your first action

An action watches the game text, and runs when it sees a match. Let's show a big message when you say hello.

**1. Open your actions file:**

```bash
nano ~/3kdb/chars/byron/actions.tin
```

**2. Add this between the `open` and `close` lines:**

```text
#action {^You say: hello everyone}
{
    #showme {<ffa>--- MY ACTION WORKED ---<088>};
};
```

**3. Save it, and run `.reload` or `#read chars/byron/actions.tin` in the game.**

**4. Run `hi`.** You should see your message appear.

**What the parts mean:**

- `#action` starts it.
- The first `{ }` is the text to look for.
- `^` means "at the very start of the line".
- The second `{ }` is what to do.
- `#showme` shows text to you only. Nobody else sees it.
- `<ffa>` sets a colour, and `<088>` puts it back to normal. Run `colors` to see your options.

### Actions that catch words

`%*` matches any text and `%w` matches one word. Each one you use is saved as `%1`, `%2`, and so on.

```text
#action {^You say: pick %*$}
{
    #var last_pick {%1};
    #showme {<afa>You picked: $last_pick<088>};
};
```

Now `say pick gold ring` shows `You picked: gold ring`.

`$` at the end of the pattern means "at the very end of the line".

### Be careful with actions

- **Match as exactly as you can.** A loose pattern can fire on chat, so someone could set off your action just by saying something. Using `^` helps a lot.
- **Don't make loops.** If your action says something that sets off the same action, it will run forever. If it happens, type this and press Enter to remove all your actions, then fix the file and run `.reload` or `#read chars/byron/actions.tin`:
  ```text
  #class {player_actions} {kill}
  ```
- **Only one action fires per line of text.** If 3kdb already has an action on the same line, yours may not run. To fire first, add a priority as a third `{ }`. Lower numbers go first, and the default is 5:
  ```text
  #action {^You say: first}
  {
      #showme {<ffa>I go first<088>};
  } {1};
  ```
- **Follow the [game rules](#game-rules-you-must-know).** No anti-idle triggers or timers, and don't let an action take other players' kills or loot.

### Variables

A variable stores something so you can use it later. `#var` sets it, and `$name` uses it.

```text
#var my_target {rat};

#alias {setkill}
{
    #var my_target {%1};
    #showme {<ffa>Target is now: $my_target<088>};
};
```

Now `setkill goblin` remembers `goblin` until your next reload or login.

3kdb keeps your stats in variables too, such as `$my[hp][current]`, your current health.

### Making decisions

`#if` runs code only when something is true, and `#else` handles the other case. It works in aliases and actions.

```text
#alias {checkhp}
{
    #if {$my[hp][current] < 100}
    {
        #showme {<faa>HP is low: $my[hp][current]<088>};
    };
    #else
    {
        #showme {<afa>HP is fine: $my[hp][current]<088>};
    };
};
```

To compare words, use double quotes on both sides:

```text
#alias {guildcheck}
{
    #if {"$guild" == "bard"}
    {
        #showme {<afa>You are a bard<088>};
    };
};
```

### Colour, hide or change text

These go in `actions.tin`, between the `open` and `close` lines.

**Colour a line:**

```text
#highlight {^You say: bright} {<ffa>};
```

**Hide a line:**

```text
#gag {^You say: secret};
```

**Change a line:**

```text
#substitute {^You say: oldword} {You say: NEWWORD};
```

### Check something every round

Your `heartbeat.tin` runs over and over during play, every couple of seconds or more often. The file has the right layout already, with notes in it. Put things inside the section it marks, so the deadman can stop them when you're away. For example:

```text
#alias {_player_heartbeat}
{
    #if !$idle_flag
    {
        #if {$my[hp][current] < 500}
        {
            #showme {<faa>Low health!<088>};
        };
    };
};
```

This example shows its message again and again while your health is low, which is why anything in this file needs care. You could use your own command in place of `#showme`, such as drinking a potion, but check the file's notes first for how to run something only once per round. **Replace** the file's existing `_player_heartbeat` with your version instead of adding a second one, because only the last one counts.

### Bot hooks

Your `config.tin` has two aliases you can fill in:

```text
#alias {.pre_bot_check}
{
    #NOP -- Runs when a bot begins;
    #showme {<ffa>Bot starting<088>};
};

#alias {.pre_fight_check}
{
    #NOP -- Runs right before fighting a mob;
    #NOP;
};
```

### The deadman alias

To run your own commands when the [deadman timer](#deadman-timer) fires, add this to `aliases.tin`:

```text
#alias {_player_deadmanActions}
{
    #showme {<faa>Deadman fired!<088>};
};
```

### Load your changes

After saving a file, load it in the game with:

```text
.reload
```

That reloads your character's files and your guild's scripts. For something simple, it's quicker to load just the file you changed:

```text
#read chars/byron/aliases.tin
```

Remember that your files only change what's in the game when you reload or log back in.

### If something doesn't work

- **The game says `There is no reason to...`:** the game doesn't know that word, so your alias didn't load. Run `.reload` or `#read` the file, and check the name.
- **Check whether your alias loaded.** This shows it if it exists:
  ```text
  #alias {hi}
  ```
- **Look for a missing `;` or `}`.** Every `{` needs a matching `}`.
- **See exactly what's happening:** `debug` turns on detailed output, and `debugoff` turns it off.
- **Still stuck?** Comment things out by putting `#NOP -- ` at the start of a line, and add them back one at a time.

### Saving your code

Your character's folder stays when you update with `git pull` or `git-sync`. To keep a backup, or to share your code, see [github.md](github.md).

[Back to top](#3kdb-manual)

---

## Keeping 3kdb updated

**If you only cloned it:**

```bash
cd ~/3kdb
git pull
```

**If you have a fork, and the helpers installed:**

```bash
cd ~/3kdb
git-sync
```

Run `ld` and log back in, or run `.reload`, to load the new code. If only one file changed, you can `#read` that file instead. If you've changed project files, [github.md](github.md#keep-your-changes-and-still-update) explains how to keep your changes.

[Back to top](#3kdb-manual)

---

## Where everything lives

- **`startmenu.tin`:** the menu you start from
- **`chars/`:** one folder per character
- **`common/`:** code shared by every character
- **`common/guilds/`:** code for each guild
- **`common/bot/bots/`:** one file per bot
- **`common/map/`:** the map, and the speedrun list
- **`modules/`:** bigger features, like the map, crafting and trackers
- **`logs/`:** your chat and session logs
- **`vars/`:** the saved reboot times, door combos and Rastafan Hell's exit words, shared by all your characters
- **`scripts/`:** Python helpers, such as the one that posts to Discord
- **`docs/`:** these guides

[Back to top](#3kdb-manual)

---

## Command reference

These are the commands listed in `dblib`, as of when this manual was written. Run `dblib` in the game for the newest list, and `dbinfo <command>` for details. Commands for a guild only work while you're in that guild.

### General

- `findhere`: finds where you are on the mud to correct map.
- `go`: map run to speedrun. Usage: `go <speedrun>`
- `setup_3kdb`: Recommended mud prefs and first-run 3kdb client setup.
- `dung_reset`: announce dungeon resets. Usage: `dung_reset <mj/sz/aegis/dungeonname>`
- `speedruns`: displays all available speedruns.
- `ld`: go linkdead saving certain variable values.
- `th`: check tellhist.
- `exa`: examine & search stuff. Usage: `exa <thing>`
- `cwho1`: list currently online clan members.
- `calc`: perform mathematical calculations. Usage: `calc <mathproblem> - Ex: calc 100/5*25`
- `dwitch`: duplicate witch then dove them & attack first witch.
- `sra`: examine & search room nouns using MIP.
- `roomnouns`: strip filler words from the room description and list the nouns left. Usage: `roomnouns' or roomnouns <text>`
- `gags`: setup gags for a variety of things around the mud.
- `gag+`: turn on one gag group by list name. Usage: `gag-plus then group name from gags output`
- `gag-`: turn off one gag group by list name. Usage: `gag-minus then group name from gags output`
- `gag-all`: enable every gag group in the list.
- `gag-clear`: disable every gag group in the list.
- `.gswap`: kill current guild and load new one - requires gswap vaf perk. Usage: `.gswap <guild>`
- `gswap`: swap guild in game, then load its scripts once the game confirms and save it for next login. Usage: `gswap <guild>`
- `prys_exit`: exit prysmyia room.
- `dcup`: attacks mike/duplicates creature/touchs dove rune/attacks first mike.
- `beepon`: turn on terminal beep on events (toggle beep).
- `beepoff`: turn off terminal beep on events (toggle beep).
- `qq`: toggle mouse capture for clickable UI (toggle mouseActive).
- `recover`: recover, then a hidden score updates your saved score info and logs it if toggle rounds is on. Necros: also resets circle_tracker if on and sends parser off if toggle recover_parser_off is on.
- `toggle-list`: 3kdb current toggles list.
- `toggle`: turn a toggle on or off, see toggle-list. Usage: `toggle <name>`
- `toggle-reset`: set every toggle back to its default, asks first. Usage: `toggle-reset then toggle-reset confirm`
- `themes`: list color themes or preview one. Usage: `themes or themes <name>`
- `theme`: switch to a color theme. Usage: `theme <name>`
- `colors`: show the available colors.
- `.reload`: reload your character files and guild scripts after editing them.
- `caption_view`: switch the side panel tab. Usage: `caption_view <general/bot/map>`
- `sessionlog`: log the whole game session to logs/&lt;user&gt;/sessions/&lt;char&gt;_&lt;date&gt;.log, old days zstd compressed - toggle sessionlog keeps it on for this character. Usage: `sessionlog on|off`
- `grep`: search session scrollback buffer. Usage: `grep <pattern>`
- `do_action`: run all queued actionStack entries then clear stack.
- `add_action`: queue one action table row on actionStack if name not already queued. Usage: `add_action braced table row same shape as actionStack items`
- `remove_action`: remove queued row from actionStack by matching name field. Usage: `remove_action braced table row or same name token as add_action`
- `beep`: bell if beepon flag set.
- `bagall`: bag all loose items.
- `unbagall`: remove all from bag to room.
- `useHeal`: use healing items from heal list.
- `i`: inventory summary helper.
- `los`: send lineofsight to MUD.
- `stashlist`: stash list helper with assemble hooks.
- `inputswitch`: switch input to named session. Usage: `inputswitch <session>`
- `reset_standings`: reset party standings table.
- `setsplit`: reapply split layout after resize.
- `init_screen`: full screen redraw and layout.
- `draw_all`: redraw hpbar chat caption and room strips that are toggled on.
- `caption-help`: caption panel commands help.
- `caption`: show data caption panel.
- `caption+`: caption panel next tab.
- `caption-`: caption panel previous tab.
- `deadman`: idle deadman arm disarm and timers. Usage: `deadman help for syntax`
- `deadman-help`: show deadman client help.
- `deadman-list`: list deadman presets.
- `deadman+`: add deadman named preset. Usage: `deadman+ <n>`
- `deadman-`: remove deadman preset. Usage: `deadman- <n>`
- `deadman-clear`: clear all deadman presets.
- `quest_newbie`: newbie quest helper.
- `cove_gems`: cove gems pickup run.
- `aoeon`: armour of elements on.
- `aoeoff`: armour of elements off.
- `aoeimmolate`: send immolate corpse once.
- `firebat_west`: walk west into firebat hunting loop.
- `firebat_return`: walk back out of firebat loop.
- `qt_firebat_west`: qtrance west into firebat loop.
- `qt_firebat_return`: qtrance return from firebat loop.
- `cow_run`: gather cow herds speedwalk from southwest corner.
- `dsolve`: fallout shelter door solver start with door room number. Usage: `dsolve <door number>`
- `stopdsolve`: stop fallout shelter door solver.
- `fdkey`: send saved door combo after dsolve same door number. Usage: `fdkey <door number>`
- `.fly`: Guild fly powers.
- `.land`: Land from guild fly powers.
- `zodiac_stones`: Celestial Zodiac Stone Reference.
- `zodiac_times`: Celestial Zodiac Spawn Times.
- `zodiac_balance`: sell zodiac souls and orbs split between the shrines to even out Aeonos and Zephyrak rep. Usage: `zodiac_balance [plan]`
- `.scalers`: table of your preferred scaler for every scaling dungeon.
- `.set_scaler`: set your preferred scaler for one dungeon or all of them, 0 clears it. Usage: `.set_scaler <key|all> <scaler>`
- `.clear_scalers`: clear every dungeon scaler preference back to 0.
- `.reset_scalers`: rebuild the dungeon scaler list from scratch, clears all preferences.
- `3kdb_dungeon_data`: dungeon mob class sizes by scaler with filters. Usage: `3kdb_dungeon_data <dungeon|scaler n|class size|town name|jumps|fixed|help>`
- `ddata`: short form of 3kdb_dungeon_data. Usage: `ddata help`

### Mapping

- `maphelp`: echo map helper quick reference.
- `mapon`: start live mapping: brief off, static off.
- `mapoff`: stop live mapping: brief on, static on.
- `mapsearch`: search map rooms by name and note text. Usage: `mapsearch <text>`
- `findhere2`: narrow findhere by walking one exit direction. Usage: `findhere2 <direction>`
- `findhere-auto`: findhere, then walk the exits that narrow it down until the room is found. Usage: `findhere-auto [steps] / findhere-auto stop`
- `mapexplore`: walk and map every unvisited room of an area, then save. Usage: `mapexplore [area] / mapexplore stop`
- `loadmap`: load mapper and maphelper then goto cursor vnum.
- `rotate`: Rejected Game: line the map and inductor/crack path up with the room you are in.
- `hidemap`: hide the map and give its space to the side panel, go and bots still work, saved per character.
- `showmap`: show the map again after hidemap.
- `mapgo`: move the map cursor to a speedrun without moving you. Usage: `mapgo <speedrun>`
- `mapsave`: save common/map/3k_shared.map.
- `mapload`: load common/map/3k_shared.map.
- `mapname`: rename the current room. Usage: `mapname <name>`
- `mapnote`: set the current room note. Usage: `mapnote <note>`
- `mapsym`: set the current room symbol. Usage: `mapsym <char>`
- `maparea`: set area name for the current room. Usage: `maparea <name>`
- `mapexit`: make an exit direction run a command. Usage: `mapexit <exit> <command>`
- `mapdig`: new exit and room, optional second arg links back. Usage: `mapdig <dir> [new]`
- `mapdelete`: delete an exit, unlinks and removes the room. Usage: `mapdelete <exit>`
- `mapunlink`: unlink an exit from its destination. Usage: `mapunlink <exit>`
- `maplink`: link an exit to a room vnum. Usage: `maplink <exit> <room#>`
- `mapinsert`: insert a room. Usage: `mapinsert <room#>`
- `mapm`: move the map cursor one step. Usage: `mapm <dir>`
- `infoPane`: get current room info.
- `draw-map-side`: draw the map below the chat window instead of beside it.
- `draw-map-top`: draw the map in its usual place at the top right.
- `notelist`: list every map room that has a note.
- `voidlink`: link exit to vnum and insert void between. Usage: `voidlink <dir> <vnum>`
- `hmavoid`: mark CoT portal exits avoided for pathing.
- `hmfollow`: clear avoid flags on CoT portal exits.
- `mapFull`: toggle fullscreen vtmap and area list.
- `mapUndo`: undo last map edit step.
- `mapbackup`: write dated backup map file under common map.
- `mapf`: pass through to map flag subcommand. Usage: `mapf flag name then on or off`
- `mapvnum`: echo current map cursor vnum into curvnum.
- `maplm`: create landmark label for current vnum. Usage: `maplm landmark label text`
- `mapfind`: list rooms matching pattern in desc name and note. Usage: `mapfind pattern text`
- `mappath`: map find path to pattern then path show. Usage: `mappath pattern text`
- `mapicons`: echo unicode icon palette for map symbols.
- `go_back`: map run back to vnum saved by go alias.

### Bot commands

- `whitelist`: show your VIP list, players the bot's playercheck ignores.
- `whitelist+`: add a player to your VIP list. Usage: `whitelist+ <name>`
- `whitelist-`: remove a player from your VIP list. Usage: `whitelist- <name>`
- `whitelist-clear`: clear your VIP list.
- `whitelist-party`: add your party to your VIP list.
- `whitelist-room`: add the players in this room to your VIP list.
- `bot_report`: displays the progress and spoils of the current bot.
- `playercheck`: toggles the playercheck.
- `autocollect`: toggles picking up all items.
- `botlist`: displays all available bots to run.
- `.stop`: stop and kill the bot.
- `.pause`: pauses the bot.
- `.unpause`: unpauses the bot.
- `.resume`: returns to the room that was paused and resumes the bot.
- `..`: tells the bot to walk if it stopped and you don't know why.
- `.skip`: leave the mob in this room alone and walk on, the bot fights the next mob it finds.
- `3kdb`: share current bot status on party line.
- `bcy`: current bot area cycler list.
- `bcy+`: add bot to cycler list. Usage: `bcy+ <botalias> - Ex: bcy+ smurfs`
- `bcy-`: remove bot from cycler list. Usage: `bcy+ <botalias> - Ex: bcy- smurfs`
- `botclear`: clears bot cycler.
- `nextarea`: start next area in the bot cycle list.
- `cycle`: run bot cycler step.
- `ba-necro`: preset necro bot area list.
- `scales`: print dragon scale colors already collected for ignore list.
- `addscale`: mark a dragon color to skip after smuggle scale. Usage: `addscale color name`

### Combat

- `strategy-list`: 3kdb available strategies.
- `strategy-clear`: clear strategies.
- `strategy`: run named strategy. Usage: `strategy <n>`
- `strategies`: list or manage strategies.
- `mka-help`: mob kill action help.
- `mka-on`: enable mob kill actions.
- `mka-off`: disable mob kill actions.
- `mka-all`: setup mob kill actions.
- `mka-check`: list queued mob kill actions with priorities.
- `mka-clear`: clear all mob kill action queue entries.
- `mka+`: add preset or custom action repeat once to confirm unknown name. Usage: `mka+ action name`
- `mka-`: remove action by name or list index number. Usage: `mka- name or index`
- `mka++`: raise priority of named action one step. Usage: `mka++ action name`
- `mka--`: lower priority of named action one step. Usage: `mka-- action name`
- `mka`: fire queued actions then kill target or first room mob. Usage: `mka optional mob name`

### Corpses

- `corpsetrig`: show or edit corpse_trig queue. Usage: `see corpsetrig-help`
- `corpsetrig-help`: corpse trigger help.
- `corpse_trig`: run queued corpse actions after a kill.
- `corpsetrig-all`: show active queue and guild-filtered preset list.
- `corpsetrig-on`: enable corpse_trig firing.
- `corpsetrig-off`: disable corpse_trig firing.
- `corpsetrig-clear`: clear all queued corpse actions.
- `corpsetrig+`: add preset or custom action to queue. Usage: `corpsetrig+ action name`
- `corpsetrig-`: remove action by name or slot number. Usage: `corpsetrig- name or number`
- `corpsetrig++`: raise an action priority in queue. Usage: `corpsetrig++ action name`
- `corpsetrig--`: lower an action priority in queue. Usage: `corpsetrig-- action name`
- `corpsetrig-kb`: toggle killing-blow only versus all blows.
- `dcoffin`: auto run to morgue and donate coffin.
- `dcoffin1`: donate coffin variant one.
- `dcoffin2`: donate coffin variant two.
- `check_corpses`: refresh corpse inventory state.
- `corpse_select`: unwrap deslab or uncooler next corpse by priority.
- `cooler_rotate`: move corpses into cooler with trace glyph necro uses qtrance. Usage: `cooler_rotate count or repeat digit`
- `check_box`: parse colossal box into corpses key count. Usage: `check_box storage table key`
- `corpse_select_necro`: necromancer corpse picker.

### Trackers

- `3kReport`: 3kdb kill report - reports all kills - filter last # of kills or by mob name. Usage: `3kReport' or 3kReport <#/mob>`
- `3kReport-clear`: 3kdb kill Report - clear data.
- `summonDmg`: mage summon damage report.
- `summonDmg-clear`: mage summon damage report - clear data.
- `summonDmgVaf`: mage summon damage report - requires numbers vaf perk.
- `reset_gxp`: general guild gxp tracking reset.
- `reset_xp`: xp tracker reset - kills and xp shown in the caption when no bot is running.
- `dstats`: damage tracking report - requires numbers vaf perk.
- `dreset`: reset damage tracker.
- `truckDmg-clear`: reset truck damage tracking.
- `mountDmg-clear`: reset mount damage tracking.
- `supportDmg-clear`: reset support mech damage tracking.
- `defStats`: defense tracking report.
- `istats`: item tracker extraordinaire.
- `istats_reset`: reset item tracker.
- `rounds`: combat rounds all time, this session and per guild level. Turn on with toggle rounds. Usage: `rounds`, `rounds note <text>` or `rounds check`
- `rounds-help`: what the round tracker does and its commands.
- `defStats_reset`: reset defense stats tracker.
- `spellDmg-clear`: clear spell damage tracker.
- `fdmgStats`: fremen damage approximation report - no numbers perk needed.
- `fdmgTable`: fremen damage band breakdown - optional source arg. Usage: `fdmgTable <source>`
- `fdmgReset`: reset fremen damage approximator.
- `3kReport-config`: configure kill report options.
- `3kReport+`: add kill report filter.
- `3kReport-`: remove kill report filter.
- `.reps`: reputation tracking.

### Crafting

- `jewel-lookup`: displays information about jewels (use jewel-lookup help for details). Usage: `jewel-lookup help`
- `forge-on`: forge on: activates the blacksmith forge.
- `forge-off`: forge off: deactivates the blacksmith forge.
- `ln`: list nontrivial recipe mouldings in enchanters shop (recipes that provide cxp).
- `smelter-on`: smelter on: activates the enchanting smelter.
- `gem-lookup`: displays information about gem recipes (use gem-lookup help for details). Usage: `gem-lookup help`
- `make-gem`: Badger's gem maker v6.9 (use make-gem help for details). Usage: `make-gem help`
- `miner-on`: mining on. Usage: `miner-on' then mine or minefor`
- `miner-off`: mining off.
- `mine-list`: prints ore deposit names for mine after miner-on.
- `minefor-list`: prints jewel names by ore tier for minefor after miner-on.
- `stashlist assemble`: this is a mud command with auto assemble added for frags/essence/hearts.
- `deposit-lookup`: displays information about mining deposits (use deposit-lookup help for details). Usage: `deposit-lookup help`
- `mine`: run ore deposit bot path by name after miner-on. Usage: `mine <deposit>`
- `minefor`: run jewel mining queue after miner-on. Usage: `minefor <jewel or comma list>`
- `autosmelt`: smelter auto-smelt preset after smelter-on. Usage: `autosmelt <preset>`
- `assembler`: interactive assemble helper for crafted items.
- `killforge`: unload blacksmith forge class.
- `build_golem`: start golem build sequence for named corpse. Usage: `build_golem <corpse name>`
- `fill_golem`: fill golem parts from held corpses.
- `fill-moulding`: examine moulding and unstash best quality you have.
- `farmer-on`: turn farmer script on.
- `farmer-off`: turn farmer script off, stop farming and remove everything it loaded.
- `farm`: farmer commands and auto farming, after farmer-on, type farm alone for the list. Usage: `farm <option>`
- `farmhelp`: farmer help, after farmer-on. Usage: `farmhelp <topic>`
- `farmapm`: show or set the commands a minute auto-farming averages by resting between plants, after farmer-on, 0 turns rests off. Usage: `farmapm <number>`
- `borrow-tomes`: borrow a volume of every crafting tome. Usage: `borrow-tomes <1/2/3>`
- `buy-tomes`: buy a volume of every crafting tome. Usage: `buy-tomes <1/2/3>`
- `box-tomes`: get a volume of every crafting tome from your box. Usage: `box-tomes <1/2/3>`

### Professions

- `transmute_burn`: transmute crafting mats (type 'transmute_burn' for more help).
- `transmute_burn2`: This will attempt to transmute all items except ore.
- `refk`: buys a knife then reforges it and disposes of it.
- `refs`: buys a sword then reforges it and disposes of it.
- `ref`: reforge item Actype to defense. Usage: `ref <item> <ACtype>`
- `refg`: reforge item Actype to defense on ground. Usage: `refg <item> <Actype>`
- `refk1`: reforger knife buy reforge dispose step one.
- `refk2`: reforger knife buy reforge dispose step two.
- `transmute_ug`: upgrades items to the next quality tier. Usage: `transmute_ug <jewel> <quality> Note: requires curly braces around <quality>`
- `transmute_ratios`: show transmuter ratios for jewels.
- `transmuter-stats`: transmuter color tracking.
- `.scrounge`: trappers: scrounge an item in your material order. Usage: `.scrounge <item>`
- `.scrounge-pref`: trappers: show your scrounge material order.
- `.scrounge+`: trappers: raise a material's priority. Usage: `.scrounge+ <metal/wood/hide>`
- `.scrounge-`: trappers: lower a material's priority. Usage: `.scrounge- <metal/wood/hide>`

### Chat (MIP)

- `blacklist`: block names from MIP chat window (still logged and Discord). Usage: `blacklist / blacklist+ name / blacklist- name / blacklist-clear`
- `sayhist`: check your say history.
- `chatlog emotes`: turn logging emotes to the chat log on or off.
- `mipon`: enable MIP capture class.
- `mipoff`: disable MIP capture class.

### Eternal

- `dupe`: duplicate items. Usage: `dupe <item>`
- `dc`: duplicate mobs. Usage: `dc <mob> or 'dc`
- `rd3`: reset dungeons for yourself or other players. Usage: `rd3 <mj/sz/aegis/dungeonname>`
- `ewell`: redirect all damage incoming to a mob until it explodes. Usage: `ewell <mob> or 'ewell`
- `rload`: reload unique items. Usage: `rload <cup/cooler/freezer/glimmering/feather/item>`
- `imm`: immunity to all damaging attacks upto a max of 90 rounds.
- `prot`: shrinks oversized hits compared to your max HP. Usage: `toggle with prot on or prot off, stacks up to 120 rounds, full rules on mud info protection`
- `fry`: room or single target damage with damage type equal to your mobs weakest AC. Usage: `fry <mob> or 'fry' for all targets`
- `refresh`: refresh a room that was previously defiled.
- `unload`: unload a room completely.
- `et-res`: resurrect another player or yourself. Usage: `et-res <playername/myself>`
- `tp1`: teleport yourself or party to CoT or teleport to another players party. Usage: `tp1 <myself/party/playername>`
- `tp2`: teleport present party to party member. Usage: `tp2 <playername>`
- `summ1`: summon party to you or a player to CoT. Usage: `summ1 <party/playername>`
- `summ2`: summon another players party to CoT. Usage: `summ2 <playername>`
- `em`: increase your stats upto a max of 50 percent for 1 hour.
- `hw`: xp bonus upto to a max of 32 percent for 1 hour.

### ROLM

- `rolm`: switch rolm damage by damage type or weapon type. Usage: `rolm <dmgtype/wpntype>`
- `setport`: sets an anchor to your current room.
- `port`: teleport to saved anchor point.
- `dove`: stops all combat in room.

### Chaos areas

- `charge_hat`: make waerlys velvet hat - charge capacitor - requires 23 lint.
- `makering-blue`: make a blue ring - requires axe/2 blue seeds/terras hammer.
- `makering-red`: make a red ring - requires axe/2 red seeds/terras hammer.
- `makering-white`: make a white ring - requires axe/2 white seeds/terras hammer.
- `makering-green`: make a green ring - requires axe/2 green seeds/terras hammer.
- `charmbracelet`: view charm bracelet options.

### Fantasy areas

- `gmaster`: Talk to the Grand Master.
- `shankey`: shansabyks key to unlock door.
- `banu-help`: Mystic Cloak Helper Alias.
- `banu1`: Banu Step 1: search torch/get key.
- `banu2`: Banu Step 2: search trees/east with key from step 1.
- `banu3`: Banu Step 3: search pillar/fly/grab orb - orb 1.
- `banu4`: Banu Step 4: search fountain/get journal.
- `banu5`: Banu Step 5: search pathway/enter.
- `banu6`: Banu Step 6: chat with him/give journal to knight.
- `banu7`: Banu Step 7: open powder/sprinkle powder/enter.
- `banu8`: Banu Step 8: search ivy/get dynamite.
- `banu9`: Banu Step 9: ignite dynamite/drop dynamite.
- `banu99`: Banu Step 9 part 2: kill witch/search runes/get necklace - first tag.
- `banu10`: Banu Step 10: enter with necklace from step 9 part 2.
- `banu11`: Banu Step 11: search statues/fly/pry orb/get orb - orb 2.
- `banu12`: Banu Step 12: search sigil/north after giving orb 2 to guyahi.
- `guy1`: enters code word.
- `banshee-help`: Banshee Helper Alias.
- `banshee_fear`: fear guardians.
- `banshee_dispel`: dispel magic.
- `banshee_jar`: reads runes for code word.
- `get-floaties`: Ganderei Cae: picks up floaties potion.
- `startfishing`: start fishing.
- `stopfishing`: stop fishing.
- `fishlog`: show your fishing journal, after startfishing.
- `sopem1`: enter sopem part 1.
- `sopem2`: enter sopem part 2.
- `run_uk`: undead knight book and hunt loop.
- `hell-help`: Rastafan Hell: list the hell commands and what they do.
- `hnext`: Rastafan Hell (Swirling Mists): one step toward the mountain, learning the week's exit names on the way, then scales the mountain.
- `hell`: Rastafan Hell: plane and this week's learned exit names. In the mists, n e s w u d send them (u n e head toward the mountain).
- `hellbot`: Rastafan Hell: start the hell stepper where you stand in the mists (+hell starts it from outside).
- `hellplane`: Rastafan Hell: say which plane you are on if hnext lost count. Usage: `hellplane <1-5>`
- `hellreset`: Rastafan Hell: forget the learned exit names and learn them again.

### Science areas

- `continue20`: enter lvl 20 continue code.
- `continue40`: enter lvl 40 continue code.
- `set20`: save yourself to level 20.
- `set40`: save yourself to level 40.
- `eat-caps1`: swallow one blue capsule for balangool crafts.
- `eat-caps2`: swallow blue and orange capsules.
- `eat-caps3`: swallow blue orange and green capsules.
- `gool green-armour`: make balangool green armour - requires 2 green capsules or stones.
- `gool green-helmet`: make balangool green helmet - requires 2 green capsules or stones.
- `gool green-gloves`: make balangool green gloves - requires 2 green capsules or stones.
- `gool green-boots`: make balangool green boots - requires 2 green capsules or stones.
- `gool orange-armour`: make balangool orange armour - requires 2 orange capsules or stones.
- `gool orange-helmet`: make balangool orange helmet - requires 2 orange capsules or stones.
- `gool orange-gloves`: make balangool orange gloves - requires 2 orange capsules or stones.
- `gool orange-boots`: make balangool orange boots - requires 2 orange capsules or stones.
- `gool blue-armour`: make balangool blue armour - requires 2 blue capsules or stones.
- `gool blue-helmet`: make balangool blue helmet - requires 2 blue capsules or stones.
- `gool blue-gloves`: make balangool blue gloves - requires 2 blue capsules or stones.
- `gool blue-boots`: make balangool blue boots - requires 2 blue capsules or stones.

### Debugging

- `debug`: TinTin debug all on plus send echo.
- `debugoff`: turn off debug and send hook.
- `echo_on`: echo outbound sends without full debug.
- `mipdebug`: turn on MIP debug output (toggle mipdebug).
- `mipdebugoff`: turn off MIP debug output (toggle mipdebug).
- `.tickers`: list running tickers and the time left on each.

### Guild commands

**All guilds**

- `setup_3kdb_hpbar`: send hpconfig line for MIP hpbar per guild.

**Bard**

- `fillwater`: go to angel fountain in wayhaven and fill pitcher and glass with water.
- `clear_prots`: turn off all defenses.
- `maint`: keep picked defenses and songs up via the heartbeat, picks save with ld. Usage: `maint, maint <spell>, maint off/all/clear/list`
- `maint-help`: help for maint: commands, spell names and how it works.
- `vamp`: perform vampire - damage dealt to mob is returned as healing.
- `black`: perform black - causes mob to flee. Usage: `black <target>`
- `.itune`: perform invigorating tune - short term benefit which will differ for each person. Usage: `.itune <player>`
- `pd`: perform dirge - heal karma with a corpse.
- `ag`: perform amazing grace - reduce physical harm done to you.
- `om`: perform o muse - aura of protection.
- `rd`: cast focus the rainbow & perform rainbow of death.
- `rod`: perform rainbow of death & cast focus the rainbow.
- `lotb`: perform leader of the band.
- `itf`: perform into the fire - room damage.
- `ham_bot`: toggle hammer bot on & off.
- `rod_bot`: toggle rainbow of death bot on & off.
- `prots_spells`: cast all defensive spells.
- `prots_songs`: toggle defensive songs on & off - amazing grace & o muse.
- `prots_pfe`: cast protection from evil - defense against evil align mobs.
- `prots_pfg`: cast protection from good - defense against good align mobs.
- `prots_pfn`: cast protection from neutral - defense against neutral align mobs.
- `prots_pfc`: cast protection from frost - defense against ice damage.
- `prots_pfh`: cast protection from heat - defense against fire damage.
- `prots_mb`: cast mind blank - defense against mind damage.
- `prots_hs`: cast hardened skin - defense against edged damage.
- `prots_blink`: cast blink - enemy attacking you may end up missing.
- `prots_hr`: cast harmonic regeneration - health regeneration.
- `prots_grace`: perform amazing grace - reduce physical harm done to you.
- `prots_muse`: perform o muse - aura of protection.
- `buffup`: perform all song buffs for yourself or others. Usage: `buffup <player>`
- `blades`: perform blades dance.
- `critic`: perform caustic critic.
- `ebolt`: perform energy bolt.
- `es`: empowered strikes - weapon strikes do more damage.
- `reflex_clear`: remove every reflex you have set.
- `reflex_critic`: auto cast caustic critic whenever your SP is above &lt;sp&gt; - e.g. reflex_critic 800 fires at 801+ SP. Usage: `reflex_critic <sp>`
- `reflex_ow`: auto dirge a corpse (ow) whenever your karma drops below &lt;karma&gt; - e.g. reflex_ow 300 fires at 299 or less. Usage: `reflex_ow <karma>`
- `reflex_ma`: auto martial assault whenever your karma is above &lt;karma&gt; - e.g. reflex_ma 600 fires at 601+ karma. Usage: `reflex_ma <karma>`
- `reflex_soothe`: auto soothe whenever your SP drops below &lt;sp&gt; - e.g. reflex_soothe 300 fires at 299 or less. Usage: `reflex_soothe <sp>`
- `.skills`: show the bard skill tracker, .skills reset clears it. Usage: `.skills or .skills reset`

**Elemental**

- `blast`: give blast to current enemy - unbriefed. Usage: `blast <nob>`
- `blast2`: give blast to current enemy - briefed. Usage: `blast2 <mob>`
- `gs`: check escore.
- `gs2`: check escore2.
- `acid1`: set resolve & prismatic emission with acid damage.
- `blunt1`: set resolve & prismatic emission with blunt damage.
- `edged1`: set resolve & prismatic emission with edge damage.
- `electric1`: set resolve & prismatic emission with electric damage.
- `fire1`: set resolve & prismatic emission with fire damage.
- `ice1`: set resolve & prismatic emission with ice damage.
- `mind1`: set resolve & prismatic emission with mind damage.
- `poison1`: set resolve & prismatic emission with poison damage.
- `rad1`: set resolve & prismatic emission with radiation damage.
- `energy1`: set resolve & prismatic emission with energy damage.

**Fremen**

- `donate_water`: fill & donate litterjons at shimoom.
- `donate_water1`: run to shimoom & donate water - drops all corpses from coffin/freezer/cooler and dupes them with mask.
- `fai_water`: pauses bot and drops all corpses - waits for mask split and then fai's everything.
- `fskills`: see additional information on fremen skills.
- `fremCorpse`: fremen corpse handling preset one.
- `fremCorpse2`: fremen corpse handling preset two.
- `fskills-cheap`: fremen skills list cheap mode.
- `gxp-stats`: show gxp tracking stats.
- `fskill-train`: list captured fremen skills sorted by training cost.

**Gentech**

- `fill_cpc`: transfer item to CPC and return. Usage: `fill_cpc <item name>`
- `heal_up`: run to gentech infirmary admit flow.
- `shields`: gentech shields routine.
- `gt-repair`: repair twice stabilize tactical on self or named target. Usage: `gt-repair optional target name`
- `timescan`: timescan clear set query then estimate minutes to reset from flux.
- `check_slide`: check hp sp cpc pu gates and set timeslide able flag.
- `grav_well`: smuggle inducer charge grav sequence for gravity well.

**Jedi**

- `weaponstats`: show light weapon mastery and guide lines.
- `setweaponmodetime`: set weapon mode timing.

**Juggernaut**

- `ff`: fire all nukes at current enemy.
- `cdef`: cdefend players from getting beat on. Usage: `cdef <party/player/show/clear>`
- `tj`: view toplists from assorted catagories. Usage: `tj <age/bdamage/bkill/cage/damage/gxp/jkills/recruits>`
- `stimheal1`: loop through coffin, freezer and cooler for a corpse to heal stim.
- `stimheal2`: same as stimheal1 except will pause stepper if no corpses.
- `su1`: dismiss & resummon support mech into defend mode.
- `su2`: switch support mech to assault fire & defend mech.
- `su3`: switch support mech to assault electric & defend mech.
- `summonmech`: summon a new support mech & into assault fire.
- `sd`: switch support mech into defend mode.
- `jugg_report`: echo gxp and mount lock summary from tracked rounds.
- `reset_tracking`: clear gxp vars and mount counters used by jugg report.
- `support_defense`: preset support mech to armor repair defend then support reset status.
- `support_offense`: preset support mech to powerplant mount assault fire then reset status.
- `donateSupport`: parse juggs2 list and donate support type to low-stim online juggs. Usage: `donateSupport optional type word default airdrop`

**Knight**

- `battlecry`: use a random battlecry from your list, or the guild default if it's empty.
- `battlecry+`: add a battlecry to your list. Usage: `battlecry+ <text>`
- `battlecry-`: remove a battlecry by its number. Usage: `battlecry- <number>`
- `battlecry-list`: show your battlecry list.

**Mage**

- `str_party`: cast giant strength & strength on each party member.
- `prots_mb`: cast mindblank.
- `prots_pa`: cast prismatic aura.
- `prots_ps`: cast prismatic sphere.
- `prots_MG`: cast major globe.
- `prots_mg`: cast minor globe.
- `prots_ms`: cast magnificent shield.
- `prots_pfe`: cast protection from evil.
- `prots_pfg`: cast protection from good.
- `prots_rs`: cast rhino skin.
- `prots_ss`: cast stoneskin.
- `prots_shield`: cast shield.
- `prots_armor`: cast armor.
- `prots_blink`: cast blink.
- `clear_def`: clear contingencies and turn off defenses.
- `activate_sconfig`: activate summon config.
- `clear_sconfig`: clear summon config.
- `ms`: setup summon config. Usage: `ms <config> OR ms <#/golem/a/d> - Ex: 'ms 5a' or 'ms golema' - see 'ms-help'`
- `ms-help`: help for ms: shortcuts, building your own summon config and related commands.
- `castper`: setup perform with a single target damage spell. Usage: `castper' alone will show options - castper <option>`
- `msc`: quick-set summon config digits and golem lines. Usage: `msc two digit pairs then width tokens see mage summoning aliases`
- `gc_ss`: setup stoneskin with greater contingency.
- `gc_mg`: setup major globe with greater contingency.
- `gc_shield`: setup shield with greater contingency.
- `gc_armor`: setup armor with greater contingency.
- `gc_pfg`: setup protection from good with greater contingency.
- `gc_pfe`: setup protection from evil with greater contingency.
- `gc_mantle`: setup mantle with greater contingency.
- `gc_ps`: setup prismatic sphere with greater contingency.
- `c_rs`: setup rhino skin with contingency.
- `c_mg`: setup minor globe with contingency.
- `c_shield`: setup shield with contingency.
- `c_mshield`: setup magnificent shield with contingency.
- `c_armor`: setup armor with contingency.
- `c_pfg`: setup protection from good with contingency.
- `c_pfe`: setup protection from evil with contingency.
- `c_blur`: setup blur with contingency.
- `c_blink`: setup blink with contingency.
- `c_invis`: setup invisibility with contingency.
- `clear_align`: clear prot-good and prot-evil flags in defs before recasting.
- `clear_prots`: remove entire defs table used by mage defense tracking.
- `maint`: keep picked defenses up via the heartbeat, maint setup also sets their contingencies. Usage: `maint setup, maint, maint <spell>, maint default/off/all/clear/list`
- `maint-help`: help for maint: commands, spell names and how it works.
- `summon_types`: print summon roster by slot with scroll panels.
- `summon_select`: pick summon for strategy list menu off clear or monster key. Usage: `summon_select key or off or clear or empty for menu`
- `summon_str`: giant strength on each summon stack self and golem.

**Necromancer**

- `teleport set`: set necromancer teleport anchor.
- `teleport`: necromancer teleport to saved teleport anchor.
- `preserve_remains`: preserve remains workflow.
- `topup`: top up reagents or supplies run.
- `maskNP`: mask corpse NP quick macros. Usage: `maskNP width and digit suffixes see necro aliases`
- `conjureUndead`: conjure undead.
- `qtNP`: quick teleport necro preset.
- `qtNPc`: qatrance coffin unwrap then preserve absorb. Usage: `qtNPc with no args uses defaults or give corpse count`
- `qtNPf`: qatrance freezer deslab then preserve absorb. Usage: `qtNPf with no args uses defaults or give corpse count`
- `qtNPcl`: qatrance cooler uncooler then preserve absorb. Usage: `qtNPcl with no args uses defaults or give corpse count`
- `check_chest`: necromancer chest check helper.
- `power`: send mud power and parse levels into client tables.
- `powers`: send mud powers and parse levels into client tables.
- `dsave_report`: necromancer dsave mob report.
- `iprime_tracker`: invoke prime success/fail counts. Usage: `iprime_tracker or iprime_tracker reset`
- `circle_tracker`: next circle % per round by attack, up to circle 59. Turn on with toggle circle_tracker. Usage: `circle_tracker or circle_tracker reset`
- `comt`: switch invoke damage types with comtrance. Usage: `comt <damage type>`

**Priest**

- `bless_party`: bless whole party chain.
- `fftouch`: faithful touch routine.
- `gxp_reset`: reset priest gxp and round tracking counters.
- `hp_monitor`: set party heal threshold as fraction of max hit points. Usage: `hp_monitor whole number meaning percent of max`
- `sp_monitor`: set party radiance threshold as fraction of max spell points. Usage: `sp_monitor whole number meaning percent of max`
- `buff`: cast bless and beneficence on a player. Usage: `buff <player>`
- `buff_party`: cast bless and beneficence on each party member.

**Psicorps**

- `usep`: use selected psicorps power.
- `psi_donate`: donate psi resource run.
- `maint`: keep picked psicorps powers up via the heartbeat. Usage: `maint, maint <power>, maint off/all/clear/list`
- `maint-help`: help for maint: commands, power names and how it works.
- `refill_apump`: refill astral pump flow.
- `track_regen`: track psi regen stats.
- `track_regen_reset`: reset psi regen tracker.
- `gxp_reset`: reset psicorps gxp tracker.
- `reset_pw_tracking`: reset power word tracking.
- `start_pw_tracking`: start power word tracking.
- `stop_pw_tracking`: stop power word tracking.
- `gs_powers`: after gs add tracker entries for powers you already have.
- `aa_swap`: swap animal affinity implant to named affinity. Usage: `aa_swap affinity name`

**Sii**

- `gxp_reset`: reset sii gxp tracker.

[Back to top](#3kdb-manual)
