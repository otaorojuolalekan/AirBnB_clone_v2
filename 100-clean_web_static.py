#!/usr/bin/python3
"""
Fabfile to delete out-of-date archives
keeping the most recent n archives
where n is an input from user
"""
import os
from fabric.api import lcd, local, run, env, cd

env.hosts = ['52.86.83.227', '100.24.237.214']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    old_archives = sorted(os.listdir("versions"))
    [old_archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in old_archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        # archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number) if "web_static_" in a for a in archives]
        [run("rm -rf ./{}".format(a)) for a in archives]
