# ToDoCLI

A simple to-do list CLI built with [Click](https://click.palletsprojects.com/).

## Installation

### via uv (recommended)

```bash
uv tool install git+https://github.com/aryan2-7/ToDoCLI.git
```

### via pip

```bash
pip install git+https://github.com/aryan2-7/ToDoCLI.git
```

## Usage

```bash
# Add a todo
todo add

# Add a todo with priority
todo add -n "Buy groceries" -d "Milk, eggs, bread" o

# List all todos
todo list

# Filter by priority (o/m/h/u)
todo list -p h

# Delete a todo by index
todo delete 0
```

Priorities: `o` (Optional), `m` (Medium), `h` (High), `u` (Urgent)

Todos are stored at `~/.todos/todo.txt`.

## Requirements

- Python 3.12+
- Works on macOS, Linux, and Windows
