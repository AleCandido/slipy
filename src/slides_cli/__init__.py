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

# init
update_p = subparsers.add_parser("update", help=update.help["."])
update_p.set_defaults(func=update.update)


def run_slipy():
    args = parser.parse_args()
    args.func(args)
