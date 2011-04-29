import os
from fabric.api import *

# names
env.db_name = "dcgis"
env.ve_name = "boundaries"
env.project_name = "dcgis"

# paths
env.base = os.path.abspath(os.path.dirname(__file__)) # where this fabfile lives
env.project_root = os.path.join(env.base, env.project_name) # manage.py
env.ve = os.path.dirname(env.base) # one above base

def drop_database(cmd=local):
    with settings(warn_only=True):
        cmd('dropdb %(db_name)s' % env)

def create_database(cmd=local):
    cmd('createdb -T template_postgis %(db_name)s' % env)
    
def local_bootstrap():
    drop_database(local)
    create_database(local)
    with cd(env.project_root):
        local("%(ve)s/bin/python %(project_root)s/manage.py syncdb --noinput" % env)
        local("%(ve)s/bin/python %(project_root)s/manage.py migrate" % env)
        
    print "Now run manage.py createsuperuser so you can use the admin"