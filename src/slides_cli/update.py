import pathlib

import slipy.update


def update(args):
    slipy.update.update(pathlib.Path(".").absolute())


help = {".": """Update assets according to 'presentation.toml'"""}
