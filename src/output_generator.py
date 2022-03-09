import discord


def generate_contents(linkdata_list):
    if(len(linkdata_list) > 0):
        output_lines = []
        for linkdata in linkdata_list:
            output_lines.append(
                f'| {linkdata.url} | {linkdata.author.display_name} | {linkdata.date.strftime("%m/%d/%Y - %H:%M")} |')
        return '| Link | Posted by | Date |\r| ---- | --------- | ---- |\r' + \
            '\r'.join(output_lines)
    else:
        return None


async def generate_list(context, linkdata_list, display_in_channel=False):
    contents = generate_contents(linkdata_list)
    result_message = 'No link found.'
    if(contents != None):
        result_message = f'Found: {str(len(linkdata_list))} links.\r'
        if(display_in_channel and len(contents) < 4000):
            result_message += await generate_embedded_code(contents)
        else:
            result_message += await generate_file(context, contents)
    await context.channel.send(result_message)


async def generate_embedded_code(contents):
    return f'```md\r {contents}\r```'


async def generate_file(context, contents):
    filename = f'.generated/links-for-{context.channel.name}.md'
    with open(filename, 'w') as f:
        f.write(contents)
    with open(filename, 'rb') as file:
        await context.author.send(f"Link list for #{context.channel} on {context.guild.name}", file=discord.File(file, filename))
    return 'File sent in private message.'
