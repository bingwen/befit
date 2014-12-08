from fabric.api import run, local, task, env

env.name = "befit"
env.user = "bingwen"
env.env = "befit"
env.path = "/home/bingwen/apps/befit"
env.hosts = ['befit.sbw.me']


def prepare_deploy():
    local("echo ------------------------")
    local("echo DEPLOYING %S TO PRODUCTION" % env.name)
    local("echo ------------------------")


@task
def checkout_latest():
    """Pull the latest code into the git repo and copy to a timestamped release directory"""
    run("cd %(path)s; git pull origin master" % env)


def install_requirements():
    """Install the required packages using pip"""
    run('cd %(path)s; pyenv shell %(env)s; pip install -r requirements.txt' % env)


def migrate():
    """Run our migrations"""
    run('cd %(path)s; pyenv shell %(env)s; python manage.py db upgrade' % env)


def symlink_current_release():
    """Symlink our current release, uploads and settings file"""
    pass


@task
def restart_server():
    run("supervisorctl restart %s" % env.name)


@task
def deploy():
    prepare_deploy()
    checkout_latest()
    install_requirements()
    migrate()
    symlink_current_release()
    restart_server()
