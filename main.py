import click
import pandas as pd
from src.cli import parse_channel, get_dialogs


@click.group()
def main():
    pass


main.add_command(parse_channel)
main.add_command(get_dialogs)


if __name__ == '__main__':
    main()
