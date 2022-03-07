from unicodedata import name
import discord
import ENV.tokens

client = discord.Client()


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
        url_list_output = []
        channel = message.channel
        counter = 0
        async for history_message in channel.history(limit=200):
            if 'http' in history_message.content and history_message.author != client.user:
                counter += 1
                url_list_output.append(
                    f'| {str(counter)} | {history_message.content} | {history_message.author} | {history_message.created_at} |')

        await message.channel.send('Found: ' + str(counter) + ' links.')
        if(counter > 0):
            contents = '```md\r| # | Link | Posted by | Date |\r| - | ---- | ----------- | ---- |\r' + \
                '\r'.join(url_list_output) + '\r```'
            if(len(contents) < 4000 or ' --file' in message.content):
                await message.channel.send(contents)
            else:
                filename = 'links-for-'+channel.name + '.md'
                with open(filename, 'w') as f:
                    f.write(contents)
                with open(filename, 'rb') as file:
                    await message.author.send(file=discord.File(file, filename))
                await message.channel.send("File containing all links sent in private message.")

client.run(ENV.tokens.BOT_TOKEN)
