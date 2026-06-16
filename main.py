import click

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
@click.argument("todofile", type=click.Path(exists=False), required =0)
@click.option("--name", "-n", prompt = "Enter the name of the todo item", help="The name of the todo item")
@click.option("--description", "-d", prompt = "Enter the description of the todo item", help="The description of the todo item")
def add(priority, todofile, name, description):
    filename = todofile if todofile else "todo.txt"
    with open(filename, "a+") as f:
        f.write(f"{PRIORITIES[priority]}: {name}: {description}\n")
    click.echo(f"Todo item added to {filename}")



@click.command()
@click.argument("idx", type=int, required = True)
def delete(idx):
    with open("todo.txt", "r") as f:
        lines = f.readlines()
        lines.pop(idx)
    with open("todo.txt", "w") as f:
        f.writelines(lines)
    click.echo(f"Todo item {idx} deleted")


@click.command()
@click.option("--priority", "-p", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=True), required = 0)
def list(priority, todofile):
    filename = todofile if todofile is not None else "todo.txt"
    with open(filename, "r") as f:
        todo_list = f.readlines()
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