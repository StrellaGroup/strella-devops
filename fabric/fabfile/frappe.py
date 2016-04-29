from fabric.api import *
from fabric.context_managers import *


# List down hosts here with the following format user@host:port
def production():
    env.hosts = []

# List down hosts here with the following format user@host:port
def staging():
    env.hosts = []

@task
def upgrade():
    env.use_ssh_config = True
    with settings(warn_only=True):
        if (run('test -d ~/frappe-bench').succeeded
            and run('which bench').succeeded):
           with cd('~/frappe-bench'):
            run('bench upgrade')
