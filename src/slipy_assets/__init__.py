import pathlib

import toml

from . import beamer
from . import reveal

here = pathlib.Path(__file__).parent

template_cfg = toml.load(here / "presentation.toml")
