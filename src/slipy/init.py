import pathlib

import toml

from .reveal import update

here = pathlib.Path(__file__).parent
template_cfg = toml.load(here / "presentation.toml")


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
