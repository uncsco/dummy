import CONF

import sys
import time
sys.path.insert(0, CONF.SRC)

##from cogapp import Cog
##from rich.progress import Progress, SpinnerColumn, TextColumn
import typer

#from dummy import X, Y, Z; print(f"{X} {Y} {Z}");  # // OKAY


app = typer.Typer(
    rich_markup_mode='rich',  #// https://typer.tiangolo.com/tutorial/commands/help/#rich-markup
)

@app.command()
def hello(name: str = "World"):
    """Hello!
    """
    print(f"Hello, {name}!")

@app.command()
def hello_env(
    name: str = typer.Argument("World", envvar=['MY_NAME']),
    age: str = typer.Argument(37, envvar=['MY_AGE']),
):
    """Hello!
    - [bold]Env Vars[/bold]: [italic]https://typer.tiangolo.com/tutorial/arguments/envvar/[/italic]
    """
    print(f"Hello, {name}! You are {age}.")


if __name__ == "__main__":
    app()

