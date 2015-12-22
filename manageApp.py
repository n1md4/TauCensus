#!/usr/bin/env python

from flask.ext.script import Manager, Shell, Server
from FlaskApp import app

manager = Manager(app)

@manager.command
def createdb():
    from FlaskApp.models import db
    db.create_all()

manager.run()
