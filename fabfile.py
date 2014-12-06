from fabric.api import run, local, task, env

env.name = "shae"
env.user = "inad"
env.env = "shae"
env.path = "/home/inad/apps/shae"
env.hosts = ['x.inad.com:2201']


def prepare_deploy():
    local("echo ------------------------")
    local("echo DEPLOYING Shae TO PRODUCTION")
    local("echo ------------------------")


@task
def checkout_latest():
    """Pull the latest code into the git repo and copy to a timestamped release directory"""
    import time
    env.release = time.strftime('%Y%m%d%H%M%S')
    run("cd %(path)s/repository; git pull origin master" % env)
    run('cp -R %(path)s/repository %(path)s/releases/%(release)s; rm -rf %(path)s/releases/%(release)s/.git*' % env)
    run('cd %(path)s/releases/%(release)s; cp %(path)s/conf/local_config.py local_config.py' % env)


def install_requirements():
    """Install the required packages using pip"""
    run('cd %(path)s/releases/%(release)s; pyenv shell %(env)s; pip install -r requirements.txt' % env)


def migrate():
    """Run our migrations"""
    run('cd %(path)s/releases/%(release)s; pyenv shell %(env)s; python manage.py db upgrade' % env)


def symlink_current_release():
    """Symlink our current release, uploads and settings file"""
    run('cd %(path)s; rm releases/previous; mv releases/current releases/previous;' % env)
    run('cd %(path)s; ln -s %(release)s releases/current' % env)


@task
def restart_server():
    run("supervisorctl restart shae")


@task
def rollback():
    """
    Limited rollback capability. Simple loads the previously current
    version of the code. Rolling back again will swap between the two.
    """
    run('cd %(path)s; mv releases/current releases/_previous;' % env)
    run('cd %(path)s; mv releases/previous releases/current;' % env)
    run('cd %(path)s; mv releases/_previous releases/previous;' % env)
    restart_server()


@task
def deploy():
    prepare_deploy()
    checkout_latest()
    install_requirements()
    migrate()
    symlink_current_release()
    restart_server()
