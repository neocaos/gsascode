import click

from src.core.env import environment
from src.init import init
from src.login import login
from src.plan import plan
from src.pull import pull
from src.apply import apply


@click.group()
def gsascode():
    pass


gsascode.add_command(init)
gsascode.add_command(login)
gsascode.add_command(plan)  # GROUP
gsascode.add_command(pull)
gsascode.add_command(apply)


if __name__ == "__main__":
    gsascode()
