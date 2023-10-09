Setting up the Webhook:
Step 1: Create a server if one doesn't already exist
Step 2: Go to Server Settings
Step 3: Go to Apps -> Integrations
Step 4: Click on "View Webhooks"
Step 5: Click "New Webhook".  Update the name to something descriptive and set the channel the messages will be posted into, currently all messages will go into "general", so we'll pick that and call it webhook_general


go to a new server window..and do this:
when prompted for a password, this is your superuser password you should have setup when creating the VPS that hosts tintin
Step 1: Install python, pip, and the python requests library:
sudo apt update
sudo apt install python3 python3-pip
pip3 install requests

Step 2: Create a folder in the root of your 3k files...if you use Inix's stuff, this will be .tt/3k/scripts
Step 3: Download the python file (or copy and paste it into a file you create) from the 3kdb repo
    a) Download from https://github.com/jmitchell33/3kdb/blob/master/discordPost.py
Step 4: Make sure there's no permission issues with the file, we'll set the permissions to allow any access...cuz mud.  Navigate to where you saved the postDiscord.py file, and enter:
    sudo chmod o+rx postDiscord.py


Updating mip.tin
    Step 1:
        A) 3kdb Users - Add the following to the top of this file in your private settings, chars/your-char/private.tin

            #NOP -- Discord Message Sending;
            #NOP -- Replace the below with the webhook URL for each particular discord channel;
            #NOP -- Set these variables in the user/player variables;
            #var webhook[url][general] https://discord.com/api/webhooks/long_token;
            #var webhook[url][tells] https://discord.com/api/webhooks/long_token;
            #var webhook[url][clan] https://discord.com/api/webhooks/long_token;
            #var webhook[url][guild] https://discord.com/api/webhooks/long_token;
            #var webhook[url][high_mortal] https://discord.com/api/webhooks/long_token;
            #var webhook[url][party] https://discord.com/api/webhooks/long_token;


        B) Inix3k Users - Add the following alias, function and same webhook URLs to the top of 3k/mip.tin (or a preferred variable location)

            #function sanitizePayload {
                #NOP -- Function to remove potentially problematic characters from the payload;
                #NOP -- Maybe we can replace these with char or ascii representations to pass the desired character;
                #var tempString %0;
                #replace tempString {#} {};
                #replace tempString {$} {};
                #replace tempString {*} {};
                #replace tempString {;} {};
                #replace tempString {"} {};
                #replace tempString {`} {};
                #replace tempString {'} {};
                #replace tempString {"} {};
                #replace tempString {\} {};
                #replace tempString {/} {};
                #replace tempString {(} {[};
                #replace tempString {)} {]};
                #replace tempString {-} {_};
                #replace tempString {<} {[};
                #replace tempString {>} {]};
                #replace tempString {&} { and };
                #replace tempString {|} { or };
                #line strip #var {_santized_payload} {$tempString};
                #return $_santized_payload;
            };

            #NOP -- Discord Message Sending;
            #var webhook[url][general] https://discord.com/api/webhooks/long_token;
            #var webhook[url][tells] https://discord.com/api/webhooks/long_token;
            #var webhook[url][clan] https://discord.com/api/webhooks/long_token;
            #var webhook[url][guild] https://discord.com/api/webhooks/long_token;
            #var webhook[url][high_mortal] https://discord.com/api/webhooks/long_token;
            #var webhook[url][party] https://discord.com/api/webhooks/long_token;

            #alias postDiscord {
                #NOP -- first paramater is webook destination, second is payload;
                #var payload @sanitizePayload{%0};

                #NOP -- Update scripts/discordPost.py to where the python file is located, this depends on the root #NOP -- that tintin is called from;	
                #script {python3 scripts/discordPost.py $webhook[url][general] $payload};
                #if {"$discordChannel" != "$webhook[url][general]"} {
                    #script {python3 scripts/discordPost.py $discordChannel $payload};
                };
            };


    Step 2:
        There is an alias, update_chat, that needs to be updated...  add the following lines to update_chat
        #var discordText ${mip[comm][source]}: ${mip[comm][data]};
	    #if {$discordPost && !$ignore} {postDiscord ${discordText}};

        This should now look like:
        #ALIAS {update_chat} {
            #format {timestamp} {%t} {<108>[<268>%H<108>:<268>%M<108>]<088> };
            #if {&chat[log][] >= $chat[max]} {
                #list chat[log] del 1
            };
            #NOP remove esc chars;
            #var chat[text] %0;
            #replace {chat[text]} {\\x7B} {\uFF5B};
            #replace {chat[text]} {\\x7D} {\uFF5D};
            
            #list chat[log] ins -1 {${timestamp}$chat[text]};
            #var discordText ${mip[comm][source]}: ${mip[comm][data]};
            #if {$discordPost && !$mipgag} {postDiscord ${discordText}};
            draw_chat;
        };