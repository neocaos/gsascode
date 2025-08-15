import click
import os

from src.env import environment
from src.log import log
from src.types.format import Format



@click.command()
@click.argument("baseurl")
@click.option('--format',
              type=click.Choice(Format, case_sensitive=False),default="yaml")
@click.pass_context
def init(ctx, baseurl, format):
    target_dir = environment.get_files_dir()

    if os.path.exists(target_dir) and os.listdir(target_dir):
        click.prompt("Target Path isn't empty, right? (y/N)", default=False, type=bool)

    click.echo(f"Hello from Init ,{baseurl}")
    environment.persist("baseurl", baseurl)
    environment.persist("format",format.name)
    

    ctx.invoke(log)
