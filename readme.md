# Links Hound
A simple links scraper bot for discord. It will search all links in history and write them in a mardown file, in a table.

It's a quick project, not really polished, and it's not guaranteed to work in every context and with every edge case. 
Use at your own risk.
I have no plans yet for this project, because I only needed it for a one-shot purpose, but I may improve it in the future.

In the meantime, feel free to hack it and taylor it for your own use!

## How to install?
1. You will need python 3 and discord.py library. [Check this tutorial to install it](https://discordpy.readthedocs.io/en/latest/intro.html#installing). 
2. Create a bot on Discord by [following those steps](https://discordpy.readthedocs.io/en/stable/discord.html).
3. On step 7 on this tutorial, you will be asked to invite your bot on some server. Chose the server your want and give the bot "Read Message History" and "Send Messages" permissions.
4. Create a local file named `ENV/tokens.py`, and populate it with `BOT_TOKEN = ''`. For security reasons, never share this file, since your BOT_TOKEN is basically your bot's password.

## How to use?
1. Run the file `links_hound.py` in a terminal to start the bot. You should see a message "We have logged in as *nickname*", and the bot connected on your discord server.
2. Type the command `!GetLinks` on any channel to get all the links. The bot will send you a file containing the links and will save a local copy in the `.generated/` directory.
3. You can make the bot soft-logout and terminate by sending the command `!Stop` in private or in any channel. Or just kill the terminal where it's running.

On Linux, the run command is : `python3 links_hound.py`.
On Windows, it's : `py -3 .\links_hound.py`.

## Commands :
- `!GetLinks` To retrieved all the links in a single .md file in private message. You can add the following attributes :
- `--channel` : to get the bot response in an embedded code file on the channel, instead of having it in private message.
- `--list` : to get an ordered list by date, and by authors.
- `--list --byauthor` : to get only a ordered list of links by authors.