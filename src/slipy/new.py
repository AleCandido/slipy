import pathlib

from slipy_assets import Template, Theme

from . import utils


def new(name, framework):
    project_dir = pathlib.Path(name)
    project_dir.mkdir()

    utils.switch_framework(framework).init(name, project_dir)


def checkout_assets(folder):
    project_dir = pathlib.Path(folder)

    presentation_cfg = utils.load_cfg(project_dir)
    framework = presentation_cfg["framework"]

    assets_dir = project_dir / ".presentation"
    assets_dir.mkdir(exist_ok=True)

    template = Template(presentation_cfg["template"]["name"], framework)
    template.unpack(assets_dir)

    theme = Theme(presentation_cfg["theme"]["name"], framework)
    theme.unpack(assets_dir)
