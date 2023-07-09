#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''

from fabric.api import local, run, env, put
from datetime import datetime as dt
from os import *


env.hosts = ['52.86.83.227', '100.24.237.214']


def do_pack():
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Return:
        False - If exception or the file doesn't exist at archive_path
        True - Otherwise.
    """
    if not path.isdir("versions"):
        mkdir("versions")
    cur_time = dt.now()
    output_path = "versions/web_static_{}.tgz".format(
            dt.strftime(cur_time, "%Y%m%d%H%M%S"))
    try:
        print("Packing web_static to {}".format(output_path))
        local("tar -cvzf {} web_static".format(output_path))
        archize_size = stat(output_path).st_size
        print("web_static packed: {} -> {} Bytes"
              .format(output_path, archize_size))
    except Exception:
        output_path = None
    return output_path


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not path.exists(archive_path):
        return False
    file_name = path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version is now LIVE!')
        success = True
    except Exception:
        success = False
    return success


def deploy():
    """Archives and deploys the static files to the host servers.
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
