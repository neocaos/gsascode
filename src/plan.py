import os
import click

from src.types.modes import Mode
from src.utils.workspaces import handle_workspaces
from src.core.env import environment


@click.command()
def plan():
    
    diffs = handle_workspaces(Mode.PLAN)
    print("End!!!!!")
    pass
