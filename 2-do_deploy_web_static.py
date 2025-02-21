#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""
from fabric.api import *
import os.path

env.hosts = ['18.234.168.129', '54.89.117.18']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """distributes an archive to our web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arc = archive_path.split("/")
        base = arc[1].strip('.tgz')
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}'.format(base))
        main = "/data/web_static/releases/{}".format(base)
        sudo('tar -xzf /tmp/{} -C {}/'.format(arc[1], main))
        sudo('rm /tmp/{}'.format(arc[1]))
        sudo('mv {}/web_static/* {}/'.format(main, main))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(main))
        return True
    except Exception:
        return False
