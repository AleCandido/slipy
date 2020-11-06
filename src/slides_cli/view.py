import pathlib

import slipy.view


def view(args):
    slipy.view.view(pathlib.Path(".").absolute())


help = {".": """Update assets according to 'presentation.toml'"""}
