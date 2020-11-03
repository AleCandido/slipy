import shutil
import pathlib
import subprocess
import sys
import logging

import toml
import pygit2

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="[%(levelname)s]: %(message)s (%(name)s)",
)
logger = logging.getLogger(__name__)

reveal_cfg = toml.load("reveal.toml")


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


def get_reveal():
    url = reveal_cfg["repo"]["url"]
    tmp_folder = pathlib.Path("reveal_tmp")
    dest = pathlib.Path(".reveal_dist")

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


if __name__ == "__main__":
    get_reveal()
