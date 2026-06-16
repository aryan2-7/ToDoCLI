import click
import os

TODO_FILE = os.path.expanduser("~/.todos/todo.txt")

@click.command()
@click.option("--name", prompt="Enter your name", help="The name to say hello to.")
def hello(name):
    click.echo(f"Hello {name}!")

@click.group()
def mycommands():
    pass

PRIORITIES = {"o": "Optional", "m": "Medium", "h": "High", "u": "Urgent"}

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.option("--name", "-n", prompt="Enter the name of the todo item", help="The name of the todo item")
@click.option("--description", "-d", prompt="Enter the description of the todo item", help="The description of the todo item")
def add(priority, name, description):
    os.makedirs(os.path.dirname(TODO_FILE), exist_ok=True)
    with open(TODO_FILE, "a+") as f:
        f.write(f"{PRIORITIES[priority]}: {name}: {description}\n")
    click.echo(f"Todo item added to {TODO_FILE}")


@click.command()
@click.argument("idx", type=int, required=True)
def delete(idx):
    try:
        with open(TODO_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        click.echo("No todo list found. Nothing to delete.")
        return
    if not lines or idx < 0 or idx >= len(lines):
        click.echo(f"Invalid index: {idx}. The list has {len(lines)} items.")
        return
    removed = lines.pop(idx)
    with open(TODO_FILE, "w") as f:
        f.writelines(lines)
    click.echo(f"Deleted: {removed.strip()}")


@click.command()
@click.option("--priority", "-p", type=click.Choice(PRIORITIES.keys()))
def list(priority):
    try:
        with open(TODO_FILE, "r") as f:
            todo_list = f.readlines()
    except FileNotFoundError:
        click.echo("No todo list found.")
        return
    if priority is None:
        for idx, todo in enumerate(todo_list):
            click.echo(f"{idx}: {todo}")
    else:
        for idx, todo in enumerate(todo_list):
            if priority in todo:
                click.echo(f"{idx}: {todo}")
    click.echo(f"Total todos: {len(todo_list)}")



mycommands.add_command(add)
mycommands.add_command(hello)
mycommands.add_command(delete)
mycommands.add_command(list)

if __name__ == "__main__":
    mycommands()