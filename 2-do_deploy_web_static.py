#!/usr/bin/python3
"""
Fabscript for deployment
"""
from datetime import datetime as dt
from fabric.api import *
from os import path


env.hosts = ['52.86.83.227', '100.24.237.214']


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    dt_now = dt.now().strftime('%Y%m%d%H%M%S')


    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(dt_now))


def do_deploy(archive_path):
    """Distributes an .tgz archive through web servers
    """

    if path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))

        return True

    return False
