import pathlib
import shutil
import distutils.dir_util

import yaml
import toml

# import framewokrs
from . import beamer
from . import reveal

here = pathlib.Path(__file__).parent

template_cfg = toml.load(here / "presentation.toml")


class Template:
    def __init__(self, name, framework):
        path = here / framework / "templates" / name

        self.template = path / "template.html"
        self.structure_path = path / "structure.yaml"
        with open(self.structure_path) as f:
            self.structure = yaml.safe_load(f)
        self.examples = path / "examples"

    def unpack(self, assets_dir):
        shutil.copy2(self.template, assets_dir)
        shutil.copy2(self.structure_path, assets_dir)
        distutils.dir_util.copy_tree(str(self.examples), str(assets_dir / ".."))


class Theme:
    def __init__(self, name, framework):
        path = here / framework / "themes"
        self.style = path / (name + ".css")

    def unpack(self, assets_dir):
        shutil.copy2(self.style, assets_dir)
