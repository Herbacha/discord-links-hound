import discord
import ENV.tokens
from url_finder import get_links

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Stop'):
        await client.logout()

    if message.content.startswith('!List'):
        output_lines = []
        channel = message.channel
        guild = message.guild
        counter = 0
        async for history_message in channel.history():
            if history_message.author != client.user:
                results = get_links(history_message.content)
                if results is not None:
                    for matched_url in results:
                        counter += 1
                        output_lines.append(
                            f'| {str(counter)} | {matched_url} | {guild.get_member(int(history_message.author.id)).display_name} | {history_message.created_at.strftime("%m/%d/%Y - %H:%M")} |')

        await message.channel.send('Found: ' + str(counter) + ' links.')
        if(counter > 0):
            contents = '```md\r| # | Link | Posted by | Date |\r| - | ---- | --------- | ---- |\r' + \
                '\r'.join(output_lines) + '\r```'
            if(len(contents) < 4000 or ' --file' in message.content):
                await message.channel.send(contents)
            else:
                filename = '.generated/links-for-'+channel.name + '.md'
                with open(filename, 'w') as f:
                    f.write(contents)
                with open(filename, 'rb') as file:
                    await message.author.send(f"Link list for {channel}", file=discord.File(file, filename))
                await message.channel.send("File containing all links sent in private message.")

client.run(ENV.tokens.BOT_TOKEN)
