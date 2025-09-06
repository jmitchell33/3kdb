Welcome to Byron's Repo.  It is built with a modular approach to plug and play guilds, professions, strategies, etc. while attempting to limit dependencies (although there are quite a few).  The MIP foundation was built by Balthus with bits and pieces stolen from other repos (Inix and Krat).

Feel free to contact me on 3k if you have any questions or would like to contribute.  Enjoy!

* Balthus: https://github.com/Tim-Radcliffe/Tintin-Setup
* Inix: https://github.com/Inix3K/TinTin/
* Krat: https://github.com/Krattimus/3k/
* Flooby (3scapes) https://github.com/daagar/3Steps

Instructions on installing Tin-Tin are at the bottom.

**CONNECTING TO 3K / BASIC PLAYING**
#read chars/name/name.tin  -- For example, to play Byron, I would do #read chars/byron/byron.tin from the 'root' directory.


**ESSENTIAL STRUCTURE:**
* chars: Individual character settings.
* common: Settings shared across all characters/global stuff.
* modules: Individual script packages that do specific things, that specific characters can choose to utilize.
* logs/user: This should be the system user name, not the character.  For example, if you see on the shell line.  jerry@myVPS:/mud/chars/... you would create a folder called logs/jerry

**Getting Started**

Inside the chars folder, create a copy of the "template" folder, and rename the folder as your character's name and the playername.tin to your character's name.  There are a few variables inside the playername.tin that also need to be updated.

Using Byron as an example, the file chars/byron/playername.tin would become chars/byron/byron.tin and I would set the "guild" and "user" variables.

    #var guild bard;
    #var user byron;
    #read chars/$user/vars.tin;

    #NOP -- If discord hooks are setup set this to 1;
    #var discordPost 1;

    #NOP -- Load Common files;
    #NOP -- _load_3kdb_common is located in common/config.tin;
    #read common/index.tin;

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
    wget https://github.com/scandum/tintin/releases/download/2.02.51/tintin-2.02.51.tar.gz
    tar -zxvf tintin-2.02.51.tar.gz
    cd tt/src
    ./configure
    sudo make install

Once TinTin is installed, type 'tt++' to open it.