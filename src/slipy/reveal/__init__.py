import toml

from slipy_assets import template_cfg

from . import get


def set_initial_cfg(name):
    presentation_cfg = template_cfg.copy()

    reveal_cfg = {}
    reveal_cfg["dist_dir"] = ".reveal_dist"

    presentation_cfg["reveal"] = reveal_cfg
    presentation_cfg["title"] = name

    return presentation_cfg


def init(name, project_dir):
    cfg_path = project_dir / "presentation.toml"

    with open(cfg_path, "w") as f:
        toml.dump(set_initial_cfg(name), f)
    get.get_reveal(project_dir)
