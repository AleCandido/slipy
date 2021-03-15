# -*- coding: utf-8 -*-
import pathlib
import subprocess

import packutil as pack
from setuptools import setup, find_packages

# write version on the fly - inspired by numpy
MAJOR = 0
MINOR = 2
MICRO = 3

repo_path = pathlib.Path(__file__).absolute().parent


def compile_assets():
    httpwatcher_dir = repo_path / "src" / "slipy" / "reveal" / "httpwatcher"

    out_install = subprocess.run(
        #  ["ls"],
        ["yarn"],
        capture_output=True,
        cwd=httpwatcher_dir,
    )
    print(out_install.stdout.decode())
    out_build = subprocess.run(
        #  ["ls"],
        ["yarn", "build"],
        capture_output=True,
        cwd=httpwatcher_dir,
    )
    print(out_build.stdout.decode())


def setup_package():
    compile_assets()
    # write version
    pack.versions.write_version_py(
        MAJOR,
        MINOR,
        MICRO,
        pack.versions.is_released(repo_path),
        filename="src/slipy/version.py",
    )
    print("\n\nciao\n\n")
    # paste Readme
    with open("README.md", "r") as fh:
        long_description = fh.read()
    # do it
    setup(
        name="slipy",
        version=pack.versions.mkversion(MAJOR, MINOR, MICRO),
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
                "reveal/templates/*",  # template README.md, ...
                "reveal/templates/**/*",  # specific template files: template.html, ...
                "reveal/templates/**/**/*",  # specific template examples: 1.html, ...
                "reveal/templates/**/**/**/*",  # template examples' assets: cover.png, ...,
                "reveal/themes/*",  # themes: white.css, black.css, ...
            ],
            "slides_cli": ["tutorials/*.md"],
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
            "watchdog",
            "rich",
        ],
        setup_requires=["wheel", "pygit2"],
        extras_require={"utils": ["pyperclip", "Pillow"]},
        entry_points={
            "console_scripts": [
                "slipy=slides_cli:run_slipy",
            ],
        },
        python_requires=">=3.7",
    )


if __name__ == "__main__":
    setup_package()
