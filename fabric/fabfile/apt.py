from fabric.api import task, sudo, run, env
from fabric.colors import red
from fabric.contrib.files import exists
from fabric.contrib.console import confirm

@task
def update():
    """
    Updates the package list
    """
    sudo('apt-get update -qq')

@task
def check():
    """
    Displays package updates needed
    """
    run("""apt-get dist-upgrade -s | python -c "import sys; [sys.stderr.write(l) for l in sys.stdin.readlines()[7:] if not (l.startswith('Inst') or l.startswith('Conf'))]" """)


@task
def upgrade():
    """
    Upgrades the system, updating packages and reboots if needed
    """
    sudo('apt-get -y upgrade')
    if exists('/var/run/reboot-required') and confirm('Needs reboot, do it now?'):
        print(red('Rebooting now', True))
        sudo('reboot')
