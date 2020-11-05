import pathlib
import shutil

import toml

from slipy_assets import template_cfg
from slipy_assets.reveal import Template, Theme

from .reveal import update


def make_project():
    presentation_name = input("Choose a name for the presentation: ")

    project_dir = pathlib.Path(presentation_name)
    project_dir.mkdir()

    presentation_cfg = project_dir / "presentation.toml"
    with open(presentation_cfg, "w") as f:
        toml.dump(template_cfg, f)

    return project_dir


def init(framework):
    project_dir = make_project()
    if framework == "reveal":
        update.get_reveal(project_dir)
    elif framework == "beamer":
        pass
    else:
        raise ValueError("unknown framework selected")


def checkout_assets(folder):
    path = pathlib.Path(folder)
    presentation_cfg = toml.load(path / "presentation.toml")

    template = Template(presentation_cfg.template.name)
    shutil.copy2(template.template, path)
    shutil.copy2(template.structure_path, path)

    theme = Theme(presentation_cfg.theme.name)
    shutil.copy2(theme.style, path)
