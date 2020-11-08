"""
Build everything needed to *show* the presentation, if possible in a single file
"""
import pathlib

from jinja2 import Environment, FileSystemLoader

from slipy_assets import Template

from . import utils


def build(folder):
    folder = pathlib.Path(folder)
    presentation_cfg = utils.load_cfg(folder)
    template_name = presentation_cfg["template"]["name"]
    framework = presentation_cfg["framework"]
    template = Template(template_name, framework)

    # prepare environment
    # -------------------

    env = Environment(loader=FileSystemLoader(str(folder.absolute())))

    # load data
    # ---------

    data = {}

    data["reveal_dist"] = ".reveal_dist"
    data["theme"] = presentation_cfg["theme"]["name"]

    template.update_build_context(data, folder)

    # dump the result
    # ---------------

    template = env.get_template(".presentation/template.html")
    stream = template.stream(data)
    stream.dump(str(folder.absolute() / "index.html"))
