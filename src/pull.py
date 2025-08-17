import os
import click


from src.types.modes import Mode
from src.utils.decorators import check_reachability
from src.utils.workspaces import handle_workspaces
from src.core.env import environment


@click.command()
@check_reachability()
def pull():
    target_dir = environment.get_files_dir()
    print("TP", target_dir)

    if os.path.exists(target_dir) and os.listdir(target_dir):
        click.prompt("Target Path isn't empty, right? (y/N)", default=False, type=bool)

    handle_workspaces(Mode.DUMP)
    print("End!")
