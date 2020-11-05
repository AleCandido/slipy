import pathlib
import importlib

import toml

from . import utils


def update(folder):
    project_dir = pathlib.Path(folder)
    assets_dir = project_dir / ".presentation"

    presentation_cfg = toml.load(project_dir / "presentation.toml")
    update_template(assets_dir, presentation_cfg)
    update_theme(assets_dir, presentation_cfg)


def update_template(assets_dir, presentation_cfg):
    framework = presentation_cfg["framework"]

    name = presentation_cfg["template"]["name"]
    actions = {
        "reveal": (
            lambda: importlib.import_module(
                ".reveal.assets", package=__package__
            ).update_template(name, assets_dir)
        ),
        "beamer": (lambda: None),
    }

    utils.switch_framework(framework, actions)


def update_theme(assets_dir, presentation_cfg):
    framework = presentation_cfg["framework"]

    name = presentation_cfg["theme"]["name"]

    actions = {
        "reveal": (
            lambda: importlib.import_module(
                ".reveal.assets", package=__package__
            ).update_theme(name, assets_dir)
        ),
        "beamer": (lambda: None),
    }

    utils.switch_framework(framework, actions)
