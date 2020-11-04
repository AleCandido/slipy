import pathlib

import toml

here = pathlib.Path(__file__).parent

reveal_cfg = toml.load(here / "reveal.toml")


class Template:
    def __init__(self, name):
        path = here / "templates" / name
        self.template = path / "template.html"
        self.structure = path / "structure.yaml"


class Style:
    def __init__(self, name):
        pass
