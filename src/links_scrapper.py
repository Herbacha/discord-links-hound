from src.url_finder import get_links
from src.linkdata_model import Linkdata


async def scrap(message, client):
    retrieved_links = []
    channel = message.channel
    guild = message.guild
    async for history_message in channel.history(limit=10000):
        if history_message.author != client.user:
            results = get_links(history_message.content)
            if results is not None:
                for matched_url in results:
                    retrieved_links.append(
                        Linkdata(matched_url, guild.get_member(int(history_message.author.id)), history_message.created_at))
    return retrieved_links
