#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os
from fabric.api import env, put, run

env.hosts = ['54.144.128.131', '52.206.216.38']

def do_deploy(archive_path):
    try:
        if not os.path.isfile(archive_path):
            return False

        # Upload archive to server
        put(archive_path, '/tmp/')

        # Extract filename only
        name = archive_path.split('/')[-1].split('.')[0]

        # Create the directory
        path = "/data/web_static/releases/{}".format(name)
        run('mkdir -p {}'.format(path))

        # Uncompress the archive
        run("tar -xzf /tmp/{} -C {}".format(archive_path.split('/')[-1], path))

        # Delete the archive
        run("rm /tmp/{}".format(archive_path.split('/')[-1]))

        # Move content out of the sub-folder
        run("mv /data/web_static/releases/{}/web_static/*\
             /data/web_static/releases/{}/".format(name,name))

        # Delete the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(path))

        return True
    except Exception as e:
        print(e)
        return False

