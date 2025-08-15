import click

from src.types.modes import Mode


@click.group()
def plan():
    pass


@plan.command()
def dump():
    from src.utils.workspaces import handle_workspaces

    workspaces = handle_workspaces(mode=Mode.DUMP)
    click.echo("Hello from Dummp")
