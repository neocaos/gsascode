import click

from src.env import environment
from src.init import init
from src.auth import login
from src.plan import plan
from src.dump import dump


@click.group()
def gsascode():
    pass


gsascode.add_command(init)
gsascode.add_command(login)
gsascode.add_command(plan)  # GROUP
gsascode.add_command(dump)


if __name__ == "__main__":
    gsascode()
