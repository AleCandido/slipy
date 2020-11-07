"""
Build the object to export, consisting of a folder with:

- everything needed to *show* the presentation, if possible in a single file
- the zipped dev environment
    - this should be shipped in order to be able to edit the presentation at a
      later time

"""
import pathlib
import importlib
import shutil

from . import utils


def build(folder):
    folder = pathlib.Path(folder)
    build_dir = folder / "build"
    if build_dir.exists():
        ans = input(f"'{build_dir}' exists, do you want to overwrite? [y/N]")
        if ans.lower() not in ["y", "yes"]:
            print("nothing done")
            return
        else:
            shutil.rmtree(build_dir)

    build_dir.mkdir(exist_ok=True)
    src_dir = folder / "src_tmp"
    src_dir.mkdir()

    for f in folder.iterdir():
        if f.name not in [".reveal_dist", ".presentation", "src_tmp", "build"]:
            if f.is_dir():
                shutil.copytree(str(f.absolute()), src_dir)
            else:
                shutil.copy2(str(f.absolute()), src_dir)

    src_dir = src_dir.rename("src")
    src_dest = shutil.move(str(src_dir), build_dir)
    shutil.copytree(str(folder / ".reveal_dist"), build_dir / ".reveal_dist")
    shutil.copytree(str(folder / ".presentation"), build_dir / ".presentation")
