# -*- coding: utf-8 -*-
import pathlib

import pygit2
from setuptools import setup, find_packages

# write version on the fly - inspired by numpy
MAJOR = 0
MINOR = 1
MICRO = 2

# Further release management
# --------------------------

repo_path = pathlib.Path(__file__).absolute().parent
repo = pygit2.Repository(repo_path)

# determine ids of tagged commits
tags_commit_sha = [
    repo.resolve_refish("/".join(r.split("/")[2:]))[0].id
    for r in repo.references
    if "/tags/" in r
]
ISRELEASED = "main" in repo.head.name or repo.head.target in tags_commit_sha
SHORT_VERSION = "%d.%d" % (MAJOR, MINOR)
VERSION = "%d.%d.%d" % (MAJOR, MINOR, MICRO)


def write_version_py(filename="src/slipy/version.py"):
    cnt = """
# THIS FILE IS GENERATED FROM SETUP.PY
major = %(major)d
short_version = '%(short_version)s'
version = '%(version)s'
full_version = '%(full_version)s'
is_released = %(isreleased)s
"""
    FULLVERSION = VERSION
    if not ISRELEASED:
        FULLVERSION += "-develop"

    a = open(filename, "w")
    try:
        a.write(
            cnt
            % {
                "major": MAJOR,
                "short_version": SHORT_VERSION,
                "version": VERSION,
                "full_version": FULLVERSION,
                "isreleased": str(ISRELEASED),
            }
        )
    finally:
        a.close()


# Actual setup
# ------------


def setup_package():
    # write version
    write_version_py()
    # paste Readme
    with open("README.md", "r") as fh:
        long_description = fh.read()
    # do it
    setup(
        name="slipy",
        version=VERSION,
        description="slides utility",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="A.Candido",
        author_email="candido.ale@gmail.com",
        url="https://github.com/AleCandido/slipy",
        package_dir={"": "src"},
        packages=find_packages("src"),
        package_data={
            "slipy": ["reveal/httpwatcher/build/*.js"],
            "slipy_assets": [
                "presentation.toml",
                "reveal/reveal.toml",
                "reveal/templates/*",
                "reveal/templates/**/*",
                "reveal/templates/**/**/*",
                "reveal/themes/*",
                "reveal/themes/**/*",
            ],
        },
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
        ],
        install_requires=[
            "toml",
            "jinja2",
            "python-frontmatter",
            "pygit2",  # TODO: to be removed
            "requests",
            "websockets",
            "rich",
        ],
        setup_requires=["wheel", "pygit2"],
        entry_points={
            "console_scripts": [
                "slipy=slides_cli:run_slipy",
            ],
        },
        python_requires=">=3.7",
    )


if __name__ == "__main__":
    setup_package()
