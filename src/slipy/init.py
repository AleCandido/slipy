import pathlib

import toml

template_cfg = toml.load("presentation.toml")


def make_project():
    presentation_name = input("Choose a name for the presentation: ")

    project_dir = pathlib.Path(presentation_name)
    project_dir.mkdir()

    presentation_cfg = project_dir / "presentation.toml"
    with open(presentation_cfg, "w") as f:
        toml.dump(template_cfg, f)


def init():
    pass


if __name__ == "__main__":
    make_project()
