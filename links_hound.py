from operator import truediv
import discord
import ENV.tokens
from src.output_generator import generate_output
from src.links_scrapper import scrap


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
        print('Logging out...')
        await client.close()

    if message.content.startswith('!GetLinks'):
        retrieved_links = await scrap(message, client)
        args = message.content.split(' ')
        display_in_channel = ('--channel' in args)
        display_as_list = ('--list' in args)
        display_by_author = ('--list' in args) and ('--byauthor' in args)
        await generate_output(message, retrieved_links, display_in_channel, display_as_list, display_by_author)


client.run(ENV.tokens.BOT_TOKEN)
