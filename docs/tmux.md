# Playing in tmux

tmux keeps 3kdb running when you close your terminal or lose your connection, and lets you pick up the same game from another device. It's **optional**. Most people only need it when 3kdb runs on a server that they connect to over SSH.

Anything in a grey box is something to type or paste.

**Other guides:** [setup.md](setup.md), [manual.md](manual.md), [faq.md](faq.md), [github.md](github.md)

## Contents

- [What tmux does](#what-tmux-does)
- [Do I need it?](#do-i-need-it)
- [Install tmux](#install-tmux)
- [Settings for 3kdb](#settings-for-3kdb)
- [Start playing in tmux](#start-playing-in-tmux)
- [The tmux keys](#the-tmux-keys)
- [Leave and come back](#leave-and-come-back)
- [Switch from your PC to your phone and back](#switch-from-your-pc-to-your-phone-and-back)
- [Why the screen changes size](#why-the-screen-changes-size)
- [Take another device off](#take-another-device-off)
- [Scrolling, the mouse and selecting text](#scrolling-the-mouse-and-selecting-text)
- [Stop playing for good](#stop-playing-for-good)
- [Handy commands](#handy-commands)
- [Problems and fixes](#problems-and-fixes)

---

## What tmux does

Normally TinTin++ lives inside your terminal window. Close the window, or let your SSH connection drop, and TinTin++ closes with it. Your character goes linkdead without 3kdb saving your settings first.

tmux is a program that holds your terminal for you. You start tmux, then start 3kdb inside it. When you close the window or your connection drops, tmux keeps 3kdb running and connected to the game. Later, from the same device or a different one, you **attach** to tmux again and you're right where you left off, with your scrollback and any running bot.

The tmux "place" that 3kdb runs in is called a **session**. In this guide it's named `3k`.

[Back to top](#playing-in-tmux)

---

## Do I need it?

- **3kdb is on a server you SSH into** (a VPS, a home server, a friend's box): yes, it's worth it. Without it, every dropped connection drops your game.
- **You want to start on your PC and carry on from your phone**: yes. Both devices SSH into the machine that runs 3kdb and attach to the same tmux session.
- **You only ever play on your own PC, in its own terminal window**: no. You can skip this guide.

[Back to top](#playing-in-tmux)

---

## Install tmux

Install it on the machine that **runs 3kdb**. That's the server if you SSH into one. Your phone or laptop only needs an SSH app.

**Ubuntu, Debian and Windows (Ubuntu in WSL):**

```bash
sudo apt update
sudo apt install -y tmux
```

**Mac** with [Homebrew](https://brew.sh):

```bash
brew install tmux
```

Check it worked. You should see a version number, such as `tmux 3.4`:

```bash
tmux -V
```

[Back to top](#playing-in-tmux)

---

## Settings for 3kdb

tmux reads its settings from a file called `.tmux.conf` in your home folder. 3kdb only needs one setting. Paste this all at once:

```bash
cat >> ~/.tmux.conf <<'EOF'
# The window takes the size of the device you typed on last
set -g window-size latest
EOF
```

When two devices are attached at once, this makes the screen fit whichever one you typed on last. [Why the screen changes size](#why-the-screen-changes-size) explains it. tmux 3.1 and newer already works this way, so the line only changes things on older versions, which shrink every screen to fit the smallest device.

Everything else works out of the box: colours, the mouse, Page Up and Page Down, and 3kdb's Alt keys.

If tmux is already running, load the file without restarting:

```bash
tmux source-file ~/.tmux.conf
```

If tmux says `invalid option` or `unknown value` for `window-size`, your tmux is older than 3.1. Delete that line with `nano ~/.tmux.conf`, and always join with the `-D` command under [Take another device off](#take-another-device-off).

[Back to top](#playing-in-tmux)

---

## Start playing in tmux

Run this. It starts a session called `3k`, or joins it if it's already running:

```bash
tmux new -A -s 3k
```

The screen clears and a green bar appears along the bottom. That bar means you're inside tmux. Now start 3kdb as usual:

```bash
cd ~/3kdb
tt++ startmenu.tin
```

Use the same `tmux new -A -s 3k` every time, from any device. The first time it starts the session, and after that it joins it.

**Shortcut:** to type `3k` instead, add an alias once:

```bash
echo "alias 3k='tmux new -A -s 3k'" >> ~/.bashrc
source ~/.bashrc
```

[Back to top](#playing-in-tmux)

---

## The tmux keys

tmux keys start with **`Ctrl+b`**, called the prefix. Press `Ctrl+b`, **let go**, then press the next key. Don't hold them all together.

| Keys | What it does |
|---|---|
| `Ctrl+b` then `d` | Detach: leave tmux and keep 3kdb running |
| `Ctrl+b` then `D` (Shift+d) | Pick another attached device and take it off |
| `Ctrl+b` then `[` | tmux's own scroll mode. Press `q` to leave it |
| `Ctrl+b` then `?` | List every tmux key. Press `q` to leave it |

3kdb doesn't use `Ctrl+b` for anything, so it never clashes. On a phone, use your SSH app's **Ctrl** key, usually on an extra row above the keyboard.

[Back to top](#playing-in-tmux)

---

## Leave and come back

To step away and keep playing later, do any one of these:

- Press `Ctrl+b` then `d`. You see `[detached (from session 3k)]` and you're back at the normal prompt.
- Close the terminal window.
- Lose your connection. Nothing is lost when that happens.

**3kdb keeps running and your character stays logged in**, just as if you'd walked away from your PC. A running bot keeps going, and the deadman timer still applies to it. This isn't the same as `ld`: your character doesn't go linkdead.

To come back, SSH in again and run:

```bash
tmux new -A -s 3k
```

[Back to top](#playing-in-tmux)

---

## Switch from your PC to your phone and back

Both devices SSH into the machine that runs 3kdb. On a phone, use an SSH app such as Termius.

**1. On your PC**, start as normal:

```bash
tmux new -A -s 3k
```

Then run `tt++ startmenu.tin` in `~/3kdb` and play.

**2. Leave the PC.** Detach with `Ctrl+b` then `d`, or leave the window open. Either is fine.

**3. On your phone**, SSH in and run the same command:

```bash
tmux new -A -s 3k
```

You're in the same game. About 3 seconds later 3kdb redraws for the phone's size. When the screen is 75 columns wide or less, it switches to its phone layout.

**4. Back on your PC**, run the same command again. If the PC window was still open, click in it instead. Then **type a letter and delete it with Backspace**. The screen grows back to PC size, and 3kdb redraws for it 3 seconds later.

Don't press Enter on an empty line to wake it up, because Enter repeats your last command in 3kdb.

If the PC window was left open, the PC and phone are both attached at the same time. That's fine. Both show the same game, and either can type.

[Back to top](#playing-in-tmux)

---

## Why the screen changes size

A tmux session only has one size, but a PC screen and a phone screen are very different. When both are attached, tmux has to pick a size.

With `window-size latest`, the default since tmux 3.1, it uses **the device you typed on last**:

- **On the bigger screen (your PC):** while the phone is in charge, the game only fills a phone-sized part of it. The rest is blank, or filled with dots or lines, depending on your tmux version.
- **On the smaller screen (your phone):** while the PC is in charge, it can only show part of the PC-sized screen.

Type something on a device to make it the one in charge. 3kdb notices the new size and redraws about 3 seconds later. If the layout still looks wrong after that, type `setsplit` in the game to redraw it.

**Older tmux (before 3.1)** always uses the **smallest** attached device. That's the "my PC screen went small" problem: as long as the phone is attached, the PC stays phone-sized, even after the phone goes to sleep. Fix it with `window-size latest` from [Settings for 3kdb](#settings-for-3kdb), or take the phone off as shown below.

[Back to top](#playing-in-tmux)

---

## Take another device off

Sometimes you want only one device attached, for example when a phone that's asleep still counts as attached. Pick one of these.

**Join and take every other device off in one go:**

```bash
tmux new -A -D -s 3k
```

`tmux attach -d -t 3k` does the same thing if the session is already running.

**From inside tmux:** press `Ctrl+b` then `D` (Shift+d). You get a list of attached devices. Use the arrow keys to pick one and press Enter to take it off. Press `q` to close the list without changing anything.

**Take off every device but this one:** press `Ctrl+b`, then `:`, type this and press Enter:

```text
detach -a
```

**What the other device sees:** its screen says `[detached (from session 3k)]` and drops back to its normal prompt. If you started tmux straight from your SSH app, its connection may close. That's expected. It isn't stuck, and the game keeps running.

**If a device seems to hang:** this happens when that device's connection has already died, such as a phone that went to sleep or lost Wi-Fi. The device's old screen stays frozen until its SSH app notices the connection is gone, which can take a while. tmux itself isn't stuck: taking a frozen device off worked straight away in testing, and the game never waits for it. Close that old screen or reconnect it. You can always check what's attached with `tmux list-clients`.

[Back to top](#playing-in-tmux)

---

## Scrolling, the mouse and selecting text

- **Scrolling:** use 3kdb's own **Page Up** and **Page Down**, the same as without tmux. tmux has its own scroll mode (`Ctrl+b` then `[`), but it doesn't hold 3kdb's scrollback properly. If you end up in it, press `q` to get out.
- **Mouse:** leave tmux's mouse setting off, as it is out of the box. tmux still passes the mouse through to 3kdb, so `qq` and the clickable menu work as normal.
- **Selecting text:** hold **Shift** while you select, the same as without tmux.

[Back to top](#playing-in-tmux)

---

## Stop playing for good

1. In the game, use `ld` or `quit` as usual. See [Leaving the game](manual.md#leaving-the-game).
2. Close 3kdb: press `q` on the menu, or type `#end`.
3. Type `exit` to close the tmux session.

Don't use `tmux kill-session` while you're logged in. It closes 3kdb straight away, without the save that `ld` does.

[Back to top](#playing-in-tmux)

---

## Handy commands

These run at the normal prompt, outside tmux.

| Command | What it does |
|---|---|
| `tmux new -A -s 3k` | Join the `3k` session, or start it |
| `tmux new -A -D -s 3k` | Join it and take every other device off |
| `tmux ls` | List sessions. `(attached)` means a device is in it now |
| `tmux list-clients` | List the devices attached right now, with their sizes |
| `tmux kill-session -t 3k` | Close the session and everything in it. Use `ld` first |

[Back to top](#playing-in-tmux)

---

## Problems and fixes

**`sessions should be nested with care, unset $TMUX to force`**

You're already inside tmux. Check for the green bar at the bottom. You don't need to start it again.

**`no server running` or `can't find session: 3k`**

Nothing is running in tmux, usually because the machine restarted. `tmux new -A -s 3k` starts a fresh session. Then log in from the menu as normal.

**My PC screen went small, with dots or lines around the game**

Another device, usually your phone, is in charge of the size. Type a letter and Backspace on the PC. If it stays small, your tmux is older than 3.1 or a sleeping phone is still attached, so take it off with `Ctrl+b` then `D`, or join with `tmux new -A -D -s 3k`. See [Why the screen changes size](#why-the-screen-changes-size).

**The other device says `[detached]` or closed when I joined**

You joined with `-D` or `attach -d`, which takes other devices off. That's what it's for. Use `tmux new -A -s 3k` without `-D` to share instead.

**Joining from a new device seems to hang**

See [If a device seems to hang](#take-another-device-off). Close the frozen old screen, or join with `tmux new -A -D -s 3k`.

**`Ctrl+b` does nothing on my phone**

Use your SSH app's own Ctrl key, not the phone keyboard. Press `Ctrl+b`, let go, then press the next key.

**3kdb looks squashed after switching devices**

Wait 3 seconds for it to redraw. If it still looks wrong, type `setsplit` in the game, or make sure the device you're on is the one in charge by typing on it.

**I can't type, and there's a counter like `[0/120]` in the top corner**

You're in tmux's scroll mode, or its key list. Press `q`.

[Back to top](#playing-in-tmux)
