#!/usr/bin/python3
'''Fabric script to generate .tgz archive
and distribute it on env.host servers'''

from fabric.api import local
from datetime import datetime as dt
import os


def do_pack():
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = dt.now()
    output_path = "versions/web_static_{}.tgz".format(
            dt.strftime(cur_time, "%Y%m%d%H%M%S"))
    try:
        print("Packing web_static to {}".format(output_path))
        local("tar -cvzf {} web_static".format(output_path))
        archize_size = os.stat(output_path).st_size
        print("web_static packed: {} -> {} Bytes"
              .format(output_path, archize_size))
    except Exception:
        output_path = None
    return output_path

