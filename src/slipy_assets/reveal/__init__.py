import pathlib

import yaml
import toml

here = pathlib.Path(__file__).parent

reveal_cfg = toml.load(here / "reveal.toml")


class Template:
    def __init__(self, name):
        path = here / "templates" / name

        self.template = path / "template.html"
        self.structure_path = path / "structure.yaml"
        with open(self.structure_path) as f:
            self.structure = yaml.safe_load(f)


class Theme:
    def __init__(self, name):
        path = here / "themes"
        self.style = path / (name + ".css")
