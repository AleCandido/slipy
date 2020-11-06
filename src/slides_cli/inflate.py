import pathlib

import slipy.inflate


def inflate(args):
    slipy.inflate.inflate(pathlib.Path(".").absolute())


help = {".": """Restore develop environment from a package"""}
