#!/usr/bin/python3
""" Clean up """
from fabric.api import *

env.hosts = ['18.206.92.141', '44.192.79.41']


def do_clean(number=0):
    """ do clean up """
    start = int(number) + 1

    if start < 2:
        start = 2

    with lcd('./versions'):
        local('ls -t | tail -n +{} | xargs rm -rf'.format(start))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(start))
