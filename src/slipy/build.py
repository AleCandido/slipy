"""
Build everything needed to *show* the presentation, if possible in a single file
"""
import pathlib
import shutil

from jinja2 import Environment, FileSystemLoader

from slipy_assets import Template

from . import utils


def build(folder):
    project_dir = pathlib.Path(folder).absolute()
    build_dir = project_dir / "build"

    presentation_cfg = utils.load_cfg(project_dir)
    template_name = presentation_cfg["template"]["name"]
    framework = presentation_cfg["framework"]
    template = Template(template_name, framework)

    # prepare environment
    # -------------------

    if not (build_dir).exists():
        build_dir.mkdir()

    env = Environment(loader=FileSystemLoader(str(project_dir.absolute())))

    # load data
    # ---------

    data = {}

    data["reveal_dist"] = ".reveal_dist"
    data["theme"] = presentation_cfg["theme"]["name"]

    template.update_build_context(data, project_dir)

    # dump the result
    # ---------------

    j_template = env.get_template(".presentation/template.html")
    stream = j_template.stream(data)
    stream.dump(str(build_dir / "index.html"))

    # provide dist
    # ------------
    dist = project_dir / utils.switch_framework(framework).dist_files
    shutil.rmtree(build_dir / dist.name, ignore_errors=False)
    shutil.copytree(str(dist.absolute()), str(build_dir / dist.name))
