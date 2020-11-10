import pathlib

import slipy.build


def add_parser(subparsers):
    build_p = subparsers.add_parser("build", help=help["."])
    build_p.set_defaults(func=build)


def build(args):
    slipy.build.build(pathlib.Path(".").absolute())


help = {".": """Build the presentation"""}
