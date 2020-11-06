import pathlib

import slipy.new


def init(args):
    slipy.new.checkout_assets(pathlib.Path(".").absolute())


help = {".": """Initialize project, populate assets"""}
