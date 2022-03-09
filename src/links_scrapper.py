import discord
from src.url_finder import get_links

display_in_channel = False


async def scrap(message, client):
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

    await message.channel.send(f'Found: {str(counter)} links.')
    if(counter > 0):
        contents = '```md\r| # | Link | Posted by | Date |\r| - | ---- | --------- | ---- |\r' + \
            '\r'.join(output_lines) + '\r```'
        if(display_in_channel and len(contents) < 4000):
            await message.channel.send(contents)
        else:
            filename = '.generated/links-for-'+channel.name + '.md'
            with open(filename, 'w') as f:
                f.write(contents)
            with open(filename, 'rb') as file:
                await message.author.send(f"Link list for {channel} on {guild.name}", file=discord.File(file, filename))
            await message.channel.send("File containing all links sent in private message.")
