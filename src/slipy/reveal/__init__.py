from .. import utils
from . import assets
from . import get
from . import view


def set_initial_cfg(name):
    reveal_cfg = {}
    reveal_cfg["dist_dir"] = ".reveal_dist"
    reveal_cfg["plugins"] = ["math"]

    return reveal_cfg


gitignore = """
# reveal.js
.reveal_dist
"""


def init(project_dir, force_rebuild=False):
    get.get_reveal(project_dir, force_rebuild)


dist_files = ".reveal_dist"
dev_files = [".presentation"]


def clean(folder):
    """
    Clean unneeded generated files
    """
    pass
