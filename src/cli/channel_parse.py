from src.dependencies import client
import click


@click.command()
def get_dialogs():
    with client:
        client.loop.run_until_complete(_iter_client_dialogs())


async def _iter_client_dialogs():
    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            print(f'{dialog.id}:{dialog.title}')
