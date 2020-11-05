import slipy.new


def new(args):
    slipy.new.new(args.name[0], args.framework)


help = {".": """Create a new project""", "pdf": """create a beamer presentation"""}
