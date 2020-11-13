import pathlib

from rich.console import Console
from rich.markdown import Markdown

tutorial_dir = pathlib.Path(__file__).parent
console = Console()


def display_tutorial(name):
    path = (tutorial_dir / (name + ".md")).absolute()
    with open(path) as fd:
        tutorial_text = fd.read()

    with console.pager():
        console.print(Markdown(tutorial_text))


def available_tutorials():
    tutorials = []

    for path in tutorial_dir.iterdir():
        if path.suffix == ".md":
            tutorials.append(path.stem)

    tutorials = [".".join(t.split(".")[1:]) for t in sorted(tutorials)]

    return tutorials


def print_available_tutorials():
    tutorials = available_tutorials()

    tutext = ""
    for tut in tutorials:
        tutext += f"- {tut}\n"

    console.print("[yellow]Available tutorials[/]:")
    console.print(Markdown(tutext))
