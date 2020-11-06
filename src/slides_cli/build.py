import pathlib

import slipy.build


def build(args):
    slipy.build.build(pathlib.Path(".").absolute())


help = {".": """Build the package to be exported"""}
