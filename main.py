import click

@click.command()
@click.option("--name", prompt="Enter your name", help="The name to say hello to.")
def hello(name):
    click.echo(f"Hello {name}!")

if __name__ == "__main__":
    hello()
