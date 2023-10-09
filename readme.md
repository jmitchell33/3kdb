Welcome to Byron's Repo.  It is built with a modular approach to plug and play guilds, professions, strategies, etc. while attempting to limit dependencies (although there are quite a few).  The MIP foundation was built by Balthus with bits and pieces stolen from other repos (Inix and Krat).  

Feel free to contact me on 3k if you have any questions or would like to contribute.  Enjoy!

[Balthus:] (https://github.com/Tim-Radcliffe/Tintin-Setup)
[Inix:] (https://github.com/Inix3K/TinTin/)
[Krat:] (https://github.com/Krattimus/3k/)
[Flooby (3scapes)] (https://github.com/daagar/3Steps)


**CONNECTING TO 3K / BASIC PLAYING**
#read chars/name/name.tin  -- For example, to play Byron, I would do #read chars/byron/byron.tin from the 'root' directory.


**ESSENTIAL STRUCTURE:**
* chars: Individual character settings.
* common: Settings shared across all characters/global stuff.
* modules: Individual script packages that do specific things, that specific characters can choose to utilize.
* logs/user: This should be the system user name, not the character.  For example, if you see on the shell line.  jerry@myVPS:/mud/chars/... you would create a folder called logs/jerry

**How does this all work?**
The name.tin file (byron.tin for example) is where you set the guild and select all of the 'addons' that player has.  
Using Byron as an example:

    *#var guild bard;
    #var user byron;
    #read chars/$user/vars.tin;
    #var scaler[tacos] 91;
    #var scaler[hotel] 150;
    #var scaler[zelligar] 131;

    /* load common */
    #read common/index.tin; -- Generic helpers
    #read common/bot/bots.tin; -- Byron would like access to all the bots
    #read modules/helpers/helpers.tin; -- More helper functions

    /* load specific modules for this character */
    #read modules/professions/golem_master.tin;  --Byron is a golem master
    #read modules/corpsemanager/corpsemanager.tin;  --Byron would like to use the corpse manager module (tracks # of corpses)

    /* load guild */
    #read common/guilds/$guild/index.tin;   --This loads the bard guild, the #var guild bard; on the first line determines which guild to load
    #read common/guilds/eternal/eternal.tin; -- Byron is an Eternal and will load the eternal guild

    /* load character-specific */
    #read chars/$user/actions.tin; -- Actions are "triggers"
    #read chars/$user/aliases.tin;  -- Byron specific aliases
    #read chars/$user/config.tin;   --Config.tin
    #read chars/$user/heartbeat.tin;    -- Heartbeat is executed every round, and is where you put logic like when to heal, use a corpse, etc.
    #read chars/$user/private.tin; -- This is where you keep your top secret stuff, like the alias to assemble Durskaen.




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
