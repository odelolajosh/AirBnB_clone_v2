#!/usr/bin/python3
""" Generates a .tgz archive from the content of web static """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Packing web_static to .tgz file """
    try:
        local("mkdir -p versions")
        _datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        to = "versions/web_static_{}.tgz".format(_datetime)
        local("tar -cvzf {} web_static".format(to))
        return to
    except Exception:
        return None
