import pathlib
import shutil
import subprocess
import sys
import logging

import pygit2

from slipy_assets.reveal import reveal_cfg

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="[%(levelname)s]: %(message)s (%(name)s)",
)
logger = logging.getLogger(__name__)


def build_dist(folder):
    logger.info(f"Build dist: reveal at '{folder}'")
    try:
        logger.info(f"Install: try to build '{folder}' with yarn")
        subprocess.run(["yarn"], cwd=folder)
        subprocess.run(["yarn", "build"], cwd=folder)
    except FileNotFoundError:
        logger.info(f"Install: yarn not found, try to build '{folder}' with npm")
        subprocess.run(["npm", "install"], cwd=folder)
        subprocess.run(["npm", "run-script", "build"], cwd=folder)


def extract_essentials(folder, dest):
    logger.info(f"Export dist: from '{folder}' to '{dest}'")

    shutil.copytree(folder / "dist", dest / "dist")
    logger.debug("Export dist: copied 'dist'")

    shutil.copytree(folder / "plugin", dest / "plugin")
    logger.debug("Export dist: copied 'plugin'")


def get_reveal(project_dir):
    project_path = pathlib.Path(project_dir)

    url = reveal_cfg["repo"]["url"]
    tmp_folder = project_path / "reveal_tmp"
    dest = project_path / ".reveal_dist"

    shutil.rmtree(tmp_folder, ignore_errors=True)

    if dest.exists():
        auth = input(
            f"'{dest}' already existing, do you want to continue removing it? [Y/n]"
        )
        if auth.lower() not in ["y", "yes"]:
            print("Nothing done.")
            return
        else:
            logger.info(f"Removed: old reveal.js in '{tmp_folder}' removed")
            shutil.rmtree(dest)

    logger.info(f"Clone repo: from '{url}' into '{tmp_folder}'")
    pygit2.clone_repository(url, tmp_folder)

    build_dist(tmp_folder)
    extract_essentials(tmp_folder, dest)

    shutil.rmtree(tmp_folder)
