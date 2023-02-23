import click
from src.dependencies import client
import pandas as pd


@click.command()
@click.argument('channel-id', type=int)
@click.option('--output-file', default="messages_from_channel.csv", type=str)
def parse_channel(channel_id, output_file):
    with client:
        client.loop.run_until_complete(_iter_channel_messages(channel_id, output_file))


async def _iter_channel_messages(channel_id, output_file):
    message_dicts = []
    # Print all dialog IDs and the title, nicely formatted
    async for message in client.iter_messages(channel_id):
        if message.message is not None:
            number_of_words = len(message.message.split())
            if number_of_words > 2:
                message_dicts.append({"id": message.id,
                                      "message": message.message,
                                      "date": message.date,
                                      "media": message.media.__class__})
    pd.DataFrame(message_dicts).set_index("id").to_csv(output_file)
