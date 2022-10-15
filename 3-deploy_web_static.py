#!/usr/bin/python3
""" Full deployment """
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['18.206.92.141', '44.192.79.41']


def deploy():
    """ Deploy! """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)


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


def do_deploy(archive_path):
    """ Distributes an archive to the web servers """
    if not os.path.exists(archive_path):
        return False
    try:
        archive = archive_path.split("/")[-1]

        tmp_path = '/tmp/' + archive
        release_path = '/data/web_static/releases/{}/'.format(
            archive.partition('.')[0])

        put(archive_path, tmp_path)
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf {} -C {}'.format(tmp_path, release_path))
        run('rm {}'.format(tmp_path))
        run('mv {}web_static/* {}'.format(release_path, release_path))
        run('rm -rf {}web_static/'.format(release_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_path))

        # Task carried out successfully
        print('New version deployed!')
        return True
    except Exception:
        return False
