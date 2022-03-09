import discord
import ENV.tokens
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

    if message.content.startswith('!List'):
        await scrap(message, client)

    if message.content.startswith('!ListChan'):
        await scrap(message, client, True)

client.run(ENV.tokens.BOT_TOKEN)
