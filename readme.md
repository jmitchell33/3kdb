Welcome to Byron's Repo.  It is built with a modular approach to plug and play guilds, professions, strategies, etc. while attempting to limit dependencies (although there are quite a few).  The MIP foundation was built by Balthus with bits and pieces stolen from other repos (Inix and Krat).

Feel free to contact me on 3k if you have any questions or would like to contribute.  Enjoy!

* Balthus: https://github.com/Tim-Radcliffe/Tintin-Setup
* Inix: https://github.com/Inix3K/TinTin/
* Krat: https://github.com/Krattimus/3k/
* Flooby (3scapes) https://github.com/daagar/3Steps

Instructions on installing Tin-Tin are at the bottom.

**CONNECTING TO 3K / BASIC PLAYING**
Run tt++ startmenu.tin from the 'root' directory, pick your character and press Enter. See Getting Started below for first-time setup.


**ESSENTIAL STRUCTURE:**
* chars: Individual character settings.
* common: Settings shared across all characters/global stuff.
* modules: Individual script packages that do specific things, that specific characters can choose to utilize.
* logs/user: This should be the system user name, not the character.  For example, if you see on the shell line.  jerry@myVPS:/mud/chars/... the folder is called logs/jerry.  The start menu creates it for you.

**Getting Started**

You need TinTin++ (see Installing Tin-Tin below) and git. Then download 3kdb and open the menu:

```
cd ~
git clone https://github.com/jmitchell33/3kdb.git
cd 3kdb
tt++ startmenu.tin
```

Press Enter on [ Add ], then type your character's name, guild and password. The menu creates all the files and folders your character needs. Press Enter on your character to log in.

Once you're inside 3k, run these once per character:

```
setup_3kdb
setup_3kdb_hpbar
```

To play again later:

```
cd ~/3kdb
tt++ startmenu.tin
```

More help:
* [docs/setup.md](docs/setup.md): the full setup guide, using the menu, and fixes for common problems.
* [docs/manual.md](docs/manual.md): everything 3kdb can do, including how to make your own aliases and actions.
* [docs/faq.md](docs/faq.md): short answers to common questions and problems.
* [docs/github.md](docs/github.md): getting updates, keeping your own changes, forks and pull requests.

# Assumed Guild Defaults
A few notes on mudside defaults are assumed for each guild.

**BARDS**
* Bards assume you have the following settings:
    * bset auto_shield 1


**COMMITTING / ADDING STUFF:**
* If you want to add new things, it should assume that you would generally be working within a custom module you might be building, over time, or contributing to an existing one. So work within only that /modules/\<module\> folder. Otherwise, you are also free to add to the common guild-, eq-, and area-specific scripts in the /common/\<type\>/\<script\>.tin file. That's all fine, but please make some of your changes known or at least make sense for use as a global, non-conflicting thing. Will try to put together a more custom forum for changes, but for now can also open an Issue / Feature Request or Pull request if you want, before adding global changes. 

**TIPS:**
* If you want to edit code locally and auto-send to server on saving, use VSCode and install "SFTP" plugin, then CTRL+SHIFT+P > SFTP: Config, and enter this, replacing with your server login info

        {
            "name": "3kdb",
            "host": "3kdb.org",
            "protocol": "sftp",
            "port": 22,
            "username": "YOUR_USERNAME",
            "password": "YOUR_PASSWORD",
            "remotePath": "/home/YOUR_USERNAME/mud",
            "uploadOnSave": true,
            "ignore": [
                ".vscode",
                ".git",
                ".DS_Store",
                "logs",
                "*.swp"
            ]
        }

Then you can sync and edit the mud tintin scripts from your local VSCode, and it will upload on save. C++ language syntax for highlighting in VSCode, works decently, until someone writes a tintin highlighter for vscode. 

**Installing Tin-Tin**

# The following is for Ubuntu, but may work for your flavor of Linux:
From the shell, enter:

    mkdir tintin
    cd tintin
    sudo apt-get update
    sudo apt-get install build-essential zlib1g-dev libpcre3-dev libgnutls28-dev
    sudo apt-get build-dep tintin++
    wget https://github.com/scandum/tintin/releases/download/2.02.61/tintin-2.02.61.tar.gz
    tar -zxvf tintin-2.02.61.tar.gz
    cd tt/src
    ./configure
    sudo make install

Once TinTin is installed, type 'tt++' to open it.