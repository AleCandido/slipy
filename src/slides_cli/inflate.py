import pathlib

import slipy.inflate


def inflate(args):
    slipy.inflate.inflate(pathlib.Path(".").absolute())


help = {".": """Update assets according to 'presentation.toml'"""}
