import pathlib

import slipy.build


def build(args):
    slipy.build.build(pathlib.Path(".").absolute())


help = {".": """Update assets according to 'presentation.toml'"""}
