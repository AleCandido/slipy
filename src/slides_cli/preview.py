import pathlib

import slipy.preview


def preview(args):
    slipy.preview.preview(pathlib.Path(".").absolute())


help = {".": """Update assets according to 'presentation.toml'"""}
