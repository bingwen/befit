from flask.ext.migrate import MigrateCommand, Migrate
from flask.ext.script import Manager
from factory import create_app

from app import app
from libs.db import db

migrate = Migrate()
migrate.init_app(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
