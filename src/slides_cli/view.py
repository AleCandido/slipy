import pathlib

import slipy.view


def view(args):
    slipy.view.view(pathlib.Path(".").absolute())


help = {".": """Show a packaged presentation"""}
