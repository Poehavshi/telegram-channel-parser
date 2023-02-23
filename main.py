from telethon import TelegramClient
import click
import pandas as pd

from config import api_id, api_hash


client = TelegramClient("test-stand", api_id, api_hash)


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
async def main():
    message_dicts = []
    # Print all dialog IDs and the title, nicely formatted
    async for message in client.iter_messages(-1001754702845):
        if message.message is not None:
            number_of_words = len(message.message.split())
            if number_of_words > 2:
                message_dicts.append({"id": message.id,
                                      "message": message.message,
                                      "date": message.date,
                                      "media": message.media.__class__})
    pd.DataFrame(message_dicts).set_index("id").to_csv("messages_from_channel.csv")

with client:
    client.loop.run_until_complete(main())
