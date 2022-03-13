import discord
from src.generator_formats.formats import OutputFormat
from src.generator_formats.generate_list_by_date import generate_list_by_date
from src.generator_formats.generate_list_by_author import generate_list_by_author
from src.generator_formats.generate_table import generate_table


def generate_contents(linkdata_list, output_format=OutputFormat.TABLE):
    if(len(linkdata_list) > 0):
        if(output_format == OutputFormat.LISTBYDATE):
            return generate_list_by_date(linkdata_list)
        elif(output_format == OutputFormat.LISTBYAUTHOR):
            return generate_list_by_author(linkdata_list)
        else:
            return generate_table(linkdata_list)
    else:
        return None


async def generate_output(context, linkdata_list, display_in_channel=False, display_as_list=False, display_by_author=False):

    output_format = OutputFormat.LISTBYAUTHOR if display_by_author else OutputFormat.LISTBYDATE if display_as_list else OutputFormat.TABLE
    contents = generate_contents(linkdata_list, output_format)
    result_message = 'No link found.'
    if(contents != None):
        result_message = f'Found: {str(len(linkdata_list))} links.\r'
        if(display_in_channel and len(contents) < 4000):
            result_message += await generate_embedded_code(contents)
        else:
            result_message += await generate_file(context, contents)
    await context.channel.send(result_message)


async def generate_embedded_code(contents):
    return f'```md\r{contents}\r```'


async def generate_file(context, contents):
    filename = f'.generated/links-for-{context.channel.name}.md'
    with open(filename, 'w') as f:
        f.write(contents)
    with open(filename, 'rb') as file:
        await context.author.send(f"Link list for #{context.channel} on {context.guild.name}", file=discord.File(file, filename))
    return 'File sent in private message.'
