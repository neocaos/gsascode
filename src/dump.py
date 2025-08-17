# import click
# import os

# from src.env import environment
# from src.log import log
# from src.types.modes import Mode
# from src.utils.workspaces import handle_workspaces


# @click.command()
# @click.pass_context
# def dump(ctx):

#     target_dir = environment.get_files_dir()
#     print("TP", target_dir)

#     if os.path.exists(target_dir) and os.listdir(target_dir):
#         click.prompt("Target Path isn't empty, right? (y/N)", default=False, type=bool)

#     if environment.is_reachable():

#         handle_workspaces(Mode.DUMP)
#         print("End!")
#     return
