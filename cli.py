import click


@click.group(short_help="datamarket CLI.")
def datamarket():
    """datamarket CLI.
    """
    pass


@datamarket.command()
@click.argument("name", default="datamarket")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [datamarket]
