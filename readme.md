**ESSENTIAL STRUCTURE:**
* chars: Individual character settings.
* common: Settings shared across all characters/global stuff.
* modules: Individual script packages that do specific things, that specific characters can choose to utilize.


**RULES FOR REPO:**
* Put your character-specific stuff in /chars/\<charname\>
* Only use /* COMMENT */ for comments outside of any blocks, but use "#nop comment" format inside blocks.


**CONNECTING TO 3K / BASIC PLAYING**
* Edit tmux.sh to point to wherever you have downloaded the settings, and then in a terminal (on a system that has tmux, obviously), run './tmux.sh', and it will start a 2-pane tmux session, with mud output on the left, and chatlogs on the right. You should be presented with a list of characters from the local directory, and can choose one, and your settings in mud/chars/<char>.tin will be loaded. You can load the map with 'loadmap' (and unload with 'killmap' if you notice things getting slow), then 'showmap' to see the map, or 'hidemap' to hide it. This will be changed soon to facilitate the new #draw feature in tintin.
* COMING SOON: No more tmux... will be using #draw and #screen for everything.

# Assumed Guild Defaults
A few notes on mudside defaults are assumed for each guild.

**BARDS**
* Bards assume you have the following settings:
    * bset auto_shield 1


**COMMITTING / ADDING STUFF:**
* If you want to add new things, it should assume that you would generally be working within a custom module you might be building, over time, or contributing to an existing one. So work within only that /modules/\<module\> folder. Otherwise, you are also free to add to the common guild-, eq-, an area-specific scripts in the /common/\<type\>/\<script\>.tin file. That's all fine, but please make some of your changes known or at least make sense for use as a global, non-conflicting thing. Will try to put together a more custom forum for changes, but for now can also open an Issue / Feature Request or Pull request if you want, before adding global changes. 
* If you want to help with more formal architectures or really dive in, ask Zorbaine (rw3iss@gmail.com), help is gladly accepted. There are about 3 of us wrangling the beast that is the 3k bot.

**TIPS:**
* If you want to edit code locally and auto-send to server on saving, use VSCode and install "SFTP" plugin, then CTRL+SHIFT+P > SFTP: Config, and enter this, replacing with your server login info (ask rw3iss@gmail.com for an account if you don't have one):

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

Then you can sync and edit the mud tintin scripts from your local VSCode, and it will upload on save. C++ language syntax for highlighting in VSCode, works decently, until someone writes a tintin highlighter for vscode. Also note if you have an account on the server, tintin highlighting should be enabled by default when editing tintin files with vi or vim.


**TODO**:
* *Module System:*
    - add function helper to check if module is defined, so code can utilize other modules only if the player has them loaded, without it breaking things.
    
* *3kdb:*
    - add interface to local 3k mysql area/item/mob database, for use in-game (ooh, aah).
