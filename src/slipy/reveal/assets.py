import shutil

from slipy_assets.reveal import Template, Theme


def update_template(name, assets_dir):
    template = Template(name)
    template.unpack(assets_dir)


def update_theme(name, assets_dir):
    theme = Theme(name)

    for path in assets_dir.iterdir():
        if path.suffix == ".css":
            if path.stem == name:
                return
            path.unlink()

    theme.unpack(assets_dir)
