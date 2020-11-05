import pathlib

import toml

from slipy_assets.reveal import Template, Theme

from . import utils
from . import reveal


def new(name, framework):
    project_dir = pathlib.Path(name)
    project_dir.mkdir()

    actions = {
        "reveal": (lambda: reveal.init(name, project_dir)),
        "beamer": (lambda: None),
    }
    utils.switch_framework(framework, actions)


def checkout_assets(folder):
    project_dir = pathlib.Path(folder)
    assets_dir = project_dir / ".presentation"
    assets_dir.mkdir(exist_ok=True)
    presentation_cfg = toml.load(project_dir / "presentation.toml")

    template = Template(presentation_cfg["template"]["name"])
    template.unpack(assets_dir)

    theme = Theme(presentation_cfg["theme"]["name"])
    theme.unpack(assets_dir)
