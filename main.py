import click

from src.core.env import environment
from src.init import init
from src.login import login
from src.plan import plan
from src.pull import pull


@click.group()
def gsascode():
    pass


gsascode.add_command(init)
gsascode.add_command(login)
gsascode.add_command(plan)  # GROUP
gsascode.add_command(pull)


if __name__ == "__main__":
    gsascode()
