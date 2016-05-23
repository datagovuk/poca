from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from poca import app,  scripts
from poca.database import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0"))

manager.add_command('db', MigrateCommand)

for command in scripts.commands:
    manager.add_command(command.name, command)

if __name__ == '__main__':
    manager.run()
