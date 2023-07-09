#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''

from fabric.api import local
from datetime import datetime as dt
import os
from fabric.decorators import runs_once


# @runs_once
# def do_pack():
#     '''generates .tgz archive from the contents of the web_static folder'''
#     local("mkdir -p versions")
#     path = ("versions/web_static_{}.tgz"
#             .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
#     result = local("tar -cvzf {} web_static"
#                    .format(path))

#     if result.failed:
#         return None
#     return path

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
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output
