#!/usr/bin/python3
"""distributes archive to servers"""

from fabric.api import local, env
from datetime import datetime
from pathlib import Path
from fabric.operations import run, put

time = datetime.now()
year = time.strftime("%Y")
month = time.month
day = time.day
hour = time.hour
minute = time.minute
second = time.second
filename = "web_static_{}{}{}{}{}{}".format(year, month,
                                            day, hour, minute, second)
command = "tar -cvzf versions/{}.tgz web_static".format(filename)

env.hosts = ['ubuntu@35.190.155.240', 'ubuntu@104.196.65.224']
env.key_filename = "~/.ssh/holberton"
file_path = "versions/" + filename + ".tgz"


def do_pack():
    """creates an archive"""
    local("mkdir -p versions")
    local(command)
    my_file = Path("versions/{}.tgz".format(filename))
    if my_file.is_file():
        return "versions/{}.tgz".format(filename)
    else:
        return None


def do_deploy(archive_path):
    """deploys archive to server"""
    #try: 
    put(archive_path, '/tmp/')
    input("1")
    run('sudo mkdir /data/web_static/releases/{}'.format(filename))
    input("2")
    run('sudo tar -xvf versions/{}.tgz -C /data/web_static/releases/{}'.format(filename, filename))
    input("3")
    run('sudo rm versions/{}.tgz'.format(filename))
    input("4")
    run('sudo rm /data/web_static/current')
    run('sudo ln -s /data/web_static/releases/{} /data/web_static/current'.format(filename))
    print("New version deployed!")
    return True
#    except Exception:
#        print("exception raised")
#        return False
