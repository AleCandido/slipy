import pathlib
import re

import frontmatter

from slipy_assets import Template


def update_build_context(data, project_dir="."):
    class Slide:
        def __init__(self, metadata, content):
            self.metadata = metadata
            self.content = content

    slides_dir = pathlib.Path(project_dir)
    slides_pattern = re.compile("\d*\.(html|md)")

    slides_paths = []
    for path in slides_dir.iterdir():
        if slides_pattern.fullmatch(path.name):
            slides_paths.append(path)

    slides = []
    for slide_path in slides_paths:
        with open(slide_path) as f:
            metadata, content = frontmatter.parse(f.read())

        slide = Slide(metadata, content)
        slides.append(slide)

    data["slides"] = slides
