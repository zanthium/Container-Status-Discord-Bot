# Container-Status-Discord-Bot
This discord bot will post the status's of your docker containers every 60s showing what is or isnt running. My use case for this is for check Plex services for my friends however can be repurposed as needed. You would want to configure a cron job to kick off this script for you. There are a few attributes you will want to edit inside of the python file so that it works to your benefit. 
![docker running](https://github.com/zanthium/Container-Status-Discord-Bot/assets/57977418/d2f5f65e-9b2a-4c1d-8cd4-1ab8237ed264)

# Configuration
There are 3 different fields you will need to fill out in-order to allow this script to access your discord server and the channel you want to post in.
Server_ID = "ID_VALUE"
Right click your server on the left and select "Copy Server ID". There are 2 places to put the Server ID so make sure both places are filled out with the same Server ID.

Channel_ID = "ID_VALUE"
This can be easily missed if you arent looking out for it. You will see the following string below. The "id" section is where you put your channel ID. Once you are in your discord server right click the channel you want the bot to post in and select "Copy Channel ID".
<br> channel = discord.utils.get(server.channels, id=CHANNEL_ID)

Discord_Bot_Token
This will be at the very end of the python script. When you create your new application (bot) in the discord developer portal. You can generate a token for that bot. You will need to put that token in the value below.
<br> client.run('DISCORD_BOT_TOKEN')

# Permissions
You will need to ensure these 3 settings are configured.
![image](https://github.com/zanthium/Container-Status-Discord-Bot/assets/57977418/aa2c5741-ee85-4ef0-b272-28438a8232c9)

When you invite your discord bot to your server you will need to make sure that these settings are enabled under the 
![image](https://github.com/zanthium/Container-Status-Discord-Bot/assets/57977418/9b58a7be-4d86-4a01-bab0-1d082b51c141)

# Troubleshooting
If you get a 403 Forbidden message this can come up if the channel the bot is trying to post into is locked to a specific role. To fix this assign the allowed role to the bot in the server.

# Credit
This discord bot was inspired by gdamx's Unraid-Docker-Container-Bot-Discord. Made a quite a few tweaks of my own and was left pretty happy with the end result.
