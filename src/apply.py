import click

from src.types.modes import Mode
from src.utils.workspaces import handle_workspaces


@click.command()
def apply():
    click.echo("Hello from Apply")
    
    
    handle_workspaces(Mode.APPLY)
    
    pass
