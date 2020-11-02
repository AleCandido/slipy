import pathlib

import toml
import pygit2

reveal_cfg = toml.load("reveal.toml")


def get_repo():
    url = reveal_cfg["repo"]["url"]
    pygit2.clone_repository(url, pathlib.Path("reveal_tmp"))
