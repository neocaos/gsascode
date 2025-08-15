import click


from src.env import environment


@click.command()
def log():
    print(environment.__dict__)
