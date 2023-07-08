#!/usr/bin/python3
""" Fabric script that creates a .tgz archive
  from all the contents of the web_static folder """

from datetime import datetime as dt
from fabric.api import local


def do_pack():
    """Creates a .tgz archive from the contents
    of the web_static folder of this repo.
    """

    d = dt.now()
    now = d.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    path_to_archive = "versions/web_static_{}.tgz".format(now)
    result = local("tar -czvf {} web_static".format(path_to_archive))

    if result.succeeded:
        return path_to_archive
    else:
        return None
