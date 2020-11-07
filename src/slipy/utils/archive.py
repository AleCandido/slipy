import pathlib
import shutil

import lz4

# Register LZ4 methods
# --------------------


def _lz4_archive(base_name, base_dir, **kwargs):
    pass


def _lz4_unpack(archive_path, dest_dir, **kwargs):
    pass


shutil.register_archive_format("lz4", _lz4_archive, description="lz4 file")
shutil.register_unpack_format("lz4", _lz4_unpack, description="lz4 file")

# Higher level utilities


def compress(archive_name, root_dir=None):
    """
    Fix the format

    Parameters
    ----------
    """
    if root_dir is None:
        root_dir = archive_name
    root_dir = pathlib.Path(root_dir).absolute()


def uncompress(archive_name, dest_dir=None):
    pass
