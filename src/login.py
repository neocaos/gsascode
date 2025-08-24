import click

from src.core.env import environment
import base64


@click.command()
@click.argument("user")
@click.argument("password", envvar=["GS_PASS"])
def login(user, password):

    click.echo(f"Hello from Login with {user}, {password}")

    credentials = f"{user}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    auth_header = f"Basic {encoded_credentials}"
    click.echo(f"Authorization header: {auth_header}")
    environment.persist("auth_header", auth_header)
