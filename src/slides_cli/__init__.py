import argparse

from . import new
from . import init
from . import update
from . import preview
from . import build
from . import view
from . import inflate


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help="subcommand help")

# new
new_p = subparsers.add_parser("new", help=new.help["."])
new_p.add_argument("name", nargs=1)
new_p.add_argument("-f", "--framework", default="reveal")
new_p.add_argument("--pdf", help=new.help["pdf"])
new_p.set_defaults(func=new.new)

# init
init_p = subparsers.add_parser("init", help=init.help["."])
init_p.set_defaults(func=init.init)

# update
update_p = subparsers.add_parser("update", help=update.help["."])
update_p.set_defaults(func=update.update)

# preview
preview_p = subparsers.add_parser("preview", help=preview.help["."])
preview_p.set_defaults(func=preview.preview)

# build
build_p = subparsers.add_parser("build", help=build.help["."])
build_p.set_defaults(func=build.build)

# view
view_p = subparsers.add_parser("view", help=view.help["."])
view_p.set_defaults(func=view.view)

# inflate
inflate_p = subparsers.add_parser("inflate", help=inflate.help["."])
inflate_p.set_defaults(func=inflate.inflate)


def run_slipy():
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        print(parser.format_help())
