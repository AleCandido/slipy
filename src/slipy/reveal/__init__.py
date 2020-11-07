import toml

from slipy_assets import template_cfg

from . import get
from .. import utils


def set_initial_cfg(name):
    presentation_cfg = template_cfg.copy()

    reveal_cfg = {}
    reveal_cfg["dist_dir"] = ".reveal_dist"
    reveal_cfg["plugins"] = ["math"]

    presentation_cfg["reveal"] = reveal_cfg
    presentation_cfg["title"] = name

    return presentation_cfg


def init(name, project_dir):
    cfg_path = utils.load_cfg(project_dir)

    with open(cfg_path, "w") as f:
        toml.dump(set_initial_cfg(name), f)
    get.get_reveal(project_dir)


dev_files = [".presentation", ".reveal_dist"]


def clean(folder):
    """
    Clean unneeded generated files
    """
    pass
