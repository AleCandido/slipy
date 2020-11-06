import pathlib

import slipy.preview


def preview(args):
    slipy.preview.preview(pathlib.Path(".").absolute())


help = {".": """Run a live updating version of the presentation"""}
