# Connecting with SSH

SSH lets you type into another computer's terminal from your PC or phone. With 3kdb, it's how you play on a server, or on your home PC while you're away from it. Pair it with [tmux](tmux.md) so the game keeps running when your connection drops.

You **don't** need SSH to play on your own PC in its own terminal window, and you don't need it for GitHub either. See [Do I need an SSH key for GitHub?](#do-i-need-an-ssh-key-for-github)

Anything in a grey box is something to type or paste. **Paste with a right-click or `Ctrl+Shift+V`**, because plain `Ctrl+V` usually doesn't work in a terminal.

**Other guides:** [setup.md](setup.md), [tmux.md](tmux.md), [manual.md](manual.md), [faq.md](faq.md), [github.md](github.md)

## Contents

- [The two machines](#the-two-machines)
- [Step 1: Turn on SSH on the machine that runs 3kdb](#step-1-turn-on-ssh-on-the-machine-that-runs-3kdb)
  - [A rented server (VPS)](#a-rented-server-vps)
  - [An Ubuntu or Linux PC](#an-ubuntu-or-linux-pc)
  - [A Windows PC (3kdb in Ubuntu on WSL)](#a-windows-pc-3kdb-in-ubuntu-on-wsl)
- [Step 2: Find its address](#step-2-find-its-address)
- [Step 3: Connect](#step-3-connect)
- [Step 4: Start 3kdb](#step-4-start-3kdb)
- [Log in without a password (SSH keys)](#log-in-without-a-password-ssh-keys)
- [A short name for your server](#a-short-name-for-your-server)
- [Connecting from outside your home](#connecting-from-outside-your-home)
- [Keeping it safe](#keeping-it-safe)
- [Do I need an SSH key for GitHub?](#do-i-need-an-ssh-key-for-github)
- [Problems and fixes](#problems-and-fixes)

---

## The two machines

- **The server** is the machine that runs 3kdb. It can be a rented server (a VPS), a Linux box at home, or your own Windows PC. It stays on while you play.
- **The device** is what you type on: a laptop, another PC or a phone. It only needs an SSH app. 3kdb, TinTin++ and tmux are installed on the server, not here.

In this guide, `YOUR-USER` is your login name **on the server**, not your character name, and `192.168.1.50` is an example address. Use your own for both.

[Back to top](#connecting-with-ssh)

---

## Step 1: Turn on SSH on the machine that runs 3kdb

Pick the one that matches your server.

### A rented server (VPS)

SSH is already on. When you create the server, the provider's page shows its **IP address** and a **username**, often `root` or `ubuntu`. If it offers to add an SSH key, make one first with [Log in without a password](#log-in-without-a-password-ssh-keys) and paste in the `.pub` part.

If you were given `root`, make an everyday user to play as. Connect as root (see [Step 3](#step-3-connect)), then run these, using your own name in place of `byron`:

```bash
adduser byron
usermod -aG sudo byron
```

If you log in to root with a key, give the new user the same key, so it can log in too:

```bash
rsync --archive --chown=byron:byron ~/.ssh /home/byron
```

Type `exit`, then connect again as the new user. Then follow [setup.md](setup.md) on the server to install TinTin++, git, tmux and 3kdb.

### An Ubuntu or Linux PC

Install the SSH server. It starts straight away, and again every time the PC boots:

```bash
sudo apt update
sudo apt install -y openssh-server
```

Check it's working by connecting to itself. Type `yes` if it asks about a fingerprint, then your password. You should get a new prompt. Type `exit` to go back.

```bash
ssh localhost
```

If you've turned on Ubuntu's firewall (`ufw`), let SSH through. It's off unless you turned it on, and running this doesn't hurt either way:

```bash
sudo ufw allow ssh
```

Make sure the PC doesn't go to sleep while you're away, or you can't connect.

### A Windows PC (3kdb in Ubuntu on WSL)

Turn on SSH in **Windows** itself, not in Ubuntu. With Ubuntu on WSL, other devices can't reach an SSH server inside Ubuntu without extra network setup. Instead you SSH into Windows and type `wsl` to get to Ubuntu.

**1. Install the Windows SSH server.** Open the Start menu, type `PowerShell`, right-click it and pick **Run as administrator**. Run these one at a time:

```powershell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

```powershell
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
```

The first one can take a few minutes. It also opens port 22 in the Windows firewall for you. You can also install it from **Settings**, **System**, **Optional features**, by adding **OpenSSH Server**.

**2. Find your Windows username.** In the same PowerShell window:

```powershell
whoami
```

It shows something like `desktop-abc123\byron`. Your username is the part after the `\`, here `byron`. Your password is your Windows password, the same as your Microsoft account password if you sign in with one. **Your PIN doesn't work over SSH.**

**3. Keep Windows awake.** In **Settings**, **System**, **Power** (**Power & battery** on a laptop), set sleep to **Never** when plugged in. A sleeping PC can't be reached.

**4. Keep an Ubuntu window open on the PC while you're away.** WSL can shut Ubuntu down a few seconds after its last window closes, and that would close tmux and 3kdb with it. Leaving one Ubuntu window open on the PC keeps it running.

When you connect, you land in a Windows prompt such as `byron@DESKTOP-ABC123 C:\Users\byron>`. Type `wsl` to get to Ubuntu, then carry on with [Step 4](#step-4-start-3kdb).

[Back to top](#connecting-with-ssh)

---

## Step 2: Find its address

- **A VPS:** it's on the provider's page.
- **Ubuntu or Linux:** run this on the server. The first number, such as `192.168.1.50`, is usually the one:
  ```bash
  hostname -I
  ```
- **Windows:** run `ipconfig` in PowerShell on the PC, and use the **IPv4 Address** of the adapter that's connected, such as `192.168.1.50`. Don't use the address that `hostname -I` shows inside Ubuntu, because other devices can't reach it.

An address starting `192.168.`, `10.` or `172.` only works from devices on the **same Wi-Fi or network**. To connect from somewhere else, see [Connecting from outside your home](#connecting-from-outside-your-home).

Your router can give your PC a new address after a restart. If connecting stops working one day, check the address again. Most routers let you reserve one for the PC so it stays the same.

[Back to top](#connecting-with-ssh)

---

## Step 3: Connect

**From Windows, a Mac, Linux or Ubuntu on WSL**, SSH is built in. Open a terminal (PowerShell on Windows, Terminal on a Mac) and run:

```bash
ssh YOUR-USER@192.168.1.50
```

The first time, it asks:

```text
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Type `yes` and press Enter. That saves the server, so it won't ask again. Then type your password. **It stays invisible while you type.** That's normal.

**From a phone**, install an SSH app such as **Termius** (Android and iPhone). Add a new host, and fill in:

- **Hostname or address:** `192.168.1.50`
- **Port:** `22`
- **Username:** `YOUR-USER`
- **Password:** your password on the server

Save it, then tap it to connect. Accept the fingerprint the first time. The app's extra key row has the **Ctrl** and **Esc** keys you need for tmux.

To disconnect, type `exit`. If you're in tmux, leave it first with `Ctrl+b` then `d`, so the game keeps running.

[Back to top](#connecting-with-ssh)

---

## Step 4: Start 3kdb

Once you're connected (and have typed `wsl` on a Windows PC), start or rejoin tmux, then 3kdb:

```bash
tmux new -A -s 3k
```

```bash
cd ~/3kdb
tt++ startmenu.tin
```

If 3kdb is already running in tmux, the first command puts you straight back in the game, and you don't need the second. To leave it running, press `Ctrl+b`, let go, then press `d`. [tmux.md](tmux.md) has the full guide, including switching between your PC and your phone.

[Back to top](#connecting-with-ssh)

---

## Log in without a password (SSH keys)

This is optional. A key is a pair of files on your device: a **private** key that never leaves it, and a **public** key (ending in `.pub`) that you give to the server. Once the server has your public key, you're let in without typing a password.

**1. Make a key on your device.** Run this in a terminal on the device you connect **from**:

```bash
ssh-keygen -t ed25519
```

Press Enter to save it in the usual place. It then asks for a passphrase. You can press Enter twice for none, or type one to protect the key if someone gets your device. If it says the file already exists, you already have a key, so type `n` and use that one.

**2. Give the public key to a Linux server or VPS.**

From Linux, a Mac or Ubuntu on WSL:

```bash
ssh-copy-id YOUR-USER@192.168.1.50
```

From Windows PowerShell, which doesn't have `ssh-copy-id`, paste this all at once:

```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh YOUR-USER@192.168.1.50 "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

Both ask for your password one last time. After that, `ssh YOUR-USER@192.168.1.50` logs straight in.

**On a phone**, Termius can make a key for you in its **Keychain**. Copy its public key, then on the server paste it on its own line at the end of `~/.ssh/authorized_keys`, with `nano ~/.ssh/authorized_keys`.

**A Windows PC as the server** keeps keys in a different place, and for an administrator account the file needs special permissions. Follow Microsoft's guide: https://learn.microsoft.com/windows-server/administration/openssh/openssh_keymanagement

[Back to top](#connecting-with-ssh)

---

## A short name for your server

Instead of typing the whole address each time, you can give the server a name. On your device, open the SSH settings file:

- **Linux, a Mac or Ubuntu on WSL:** `nano ~/.ssh/config`
- **Windows PowerShell:** `notepad $env:USERPROFILE\.ssh\config`. If Notepad asks to create the file, say yes. Save it with no `.txt` on the end.

Add this, with your own address and username:

```text
Host 3k
    HostName 192.168.1.50
    User YOUR-USER
    ServerAliveInterval 60
```

Now `ssh 3k` connects. `ServerAliveInterval 60` sends a small check every minute, which stops some routers dropping a connection that's gone quiet.

[Back to top](#connecting-with-ssh)

---

## Connecting from outside your home

A home address like `192.168.1.50` only works on your own network. A VPS works from anywhere, so skip this if you use one.

The easiest safe way is **Tailscale**, which is free for personal use. It joins your devices into a private network, wherever they are, without opening anything on your router.

1. Make an account at https://tailscale.com.
2. Install it on the server and sign in.
   - **Ubuntu or Linux:**
     ```bash
     curl -fsSL https://tailscale.com/install.sh | sh
     sudo tailscale up
     ```
     It prints a link. Open it in a browser and sign in.
   - **A Windows PC:** install the Windows app from https://tailscale.com/download and sign in. Install it in Windows, not in Ubuntu, because Windows is where SSH runs.
3. Install the Tailscale app on your phone or laptop and sign in with the **same account**.
4. The app lists your devices. The server's Tailscale address starts with `100.`. Use it in place of `192.168.1.50`:
   ```bash
   ssh YOUR-USER@100.101.102.103
   ```

That address keeps working at home and away, as long as Tailscale is on for both devices.

**Opening port 22 on your router** (port forwarding) also works, but it puts your PC on the open internet, where bots try passwords on it all day. If you do it, use [SSH keys](#log-in-without-a-password-ssh-keys) and turn off password logins as shown in [Keeping it safe](#keeping-it-safe).

[Back to top](#connecting-with-ssh)

---

## Keeping it safe

- Use a strong password on the server, or better, [SSH keys](#log-in-without-a-password-ssh-keys).
- **Never share your private key** (the file without `.pub`). The `.pub` file is safe to give out.
- Keep the server up to date: `sudo apt update && sudo apt upgrade` on Ubuntu.

**Turning off password logins** on a Linux server or VPS means only your keys get in. Only do this once key login works, from every device you use. Keep your current connection open while you do it, so you can undo it if something goes wrong:

```bash
echo 'PasswordAuthentication no' | sudo tee /etc/ssh/sshd_config.d/00-no-passwords.conf
sudo systemctl restart ssh
```

Then try connecting from a **new** window. If it works, you're done. If it doesn't, undo it in the window you kept open:

```bash
sudo rm /etc/ssh/sshd_config.d/00-no-passwords.conf
sudo systemctl restart ssh
```

[Back to top](#connecting-with-ssh)

---

## Do I need an SSH key for GitHub?

No. The guides set up git with `gh auth login` and **HTTPS**, which logs you in through your browser. That's separate from connecting to your server, and you don't need an SSH key for it.

If git says `Permission denied (publickey)` when you update or push, your folder is set to use GitHub over SSH. Switch it to HTTPS. For a plain clone:

```bash
cd ~/3kdb
git remote set-url origin https://github.com/jmitchell33/3kdb.git
```

For a fork, use your own GitHub username, then run `gh auth login` as in [Part 3 of github.md](github.md#part-3-set-up-a-fork-from-scratch):

```bash
cd ~/3kdb
git remote set-url origin https://github.com/YOUR-USERNAME/3kdb.git
```

[Back to top](#connecting-with-ssh)

---

## Problems and fixes

**`Connection refused`**

The address is right, but nothing is listening for SSH. The SSH server isn't installed or isn't running. Go back to [Step 1](#step-1-turn-on-ssh-on-the-machine-that-runs-3kdb). On Windows, run `Start-Service sshd` in an administrator PowerShell.

**`Connection timed out`**, or it just hangs

The device can't reach the server at all. Check:
- The address. It may have changed, so look it up again with [Step 2](#step-2-find-its-address).
- That both are on the same network, or that Tailscale is on for both.
- That the server is on and not asleep.
- On a phone, that you're on Wi-Fi, not mobile data, unless you use Tailscale.

**`Permission denied, please try again`**

Wrong username or password. Remember the username is your login on the server, not your character name. On Windows, use your Windows password, not your PIN.

**`Permission denied (publickey)`** when connecting to your server

The server only accepts keys, and your key isn't on it. Add it with [SSH keys](#log-in-without-a-password-ssh-keys) from a device that can still log in, or through the VPS provider's web console.

**`WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`**

The server's fingerprint is different from last time. That's expected if you reinstalled the server, or the address now belongs to a different machine. If you know why it changed, clear the old one and connect again:

```bash
ssh-keygen -R 192.168.1.50
```

If you don't know why, don't connect, and ask for help first.

**I typed `wsl` and it says there's no distribution installed**

Ubuntu isn't set up for the Windows user you connected as. Install Ubuntu as in [Step 1 of setup.md](setup.md#step-1-install-tintin-and-git), signed in to Windows as the same user you connect with.

**3kdb was gone when I came back to my Windows PC**

WSL shut Ubuntu down after its last window closed, which closes tmux too. Leave an Ubuntu window open on the PC while you're away. See [A Windows PC](#a-windows-pc-3kdb-in-ubuntu-on-wsl).

**My connection drops when I leave it alone**

Add `ServerAliveInterval 60`, as in [A short name for your server](#a-short-name-for-your-server). Play inside [tmux](tmux.md), so a dropped connection never drops the game.

[Back to top](#connecting-with-ssh)
