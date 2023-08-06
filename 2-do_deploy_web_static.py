#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os
from fabrin.api import hosts, put, run, evn
env.hosts = ['54.209.26.149', '52.206.216.38']

def do_deploy(archive_path):
    try:
        if not os.path.isfile(archive_path):
            return False

        #Upload archive to server
        put(archive_path, '/tmp/')

        #Extract filename only
        name = archive_path.split('/') [-1].split('.')[0]

        #Create the directory
        path = "/data/we_static/releases/{}".format(name)
        run('mkdir {}'.format(path))

        #uncompress the archive
        run("tar -xzf /tmp/{archive_path.split('/') [-1]} -c {}".format(path))
        
        #delete the archive
        run("rm /tmp/{}".format(archive_path.split('/') [-1]))

        #delete the archive
        run( "rm /data/web_static/current")

        #create a new symbolic link
        run("ln -s{} data/web_static/current".format(path))

        return True
    except:
        return False 

