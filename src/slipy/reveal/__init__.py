from .. import utils
from . import get
from . import assets


def set_initial_cfg(name):
    reveal_cfg = {}
    reveal_cfg["dist_dir"] = ".reveal_dist"
    reveal_cfg["plugins"] = ["math"]

    return reveal_cfg


def init(project_dir):
    get.get_reveal(project_dir)


dev_files = [".presentation", ".reveal_dist"]


def clean(folder):
    """
    Clean unneeded generated files
    """
    pass
