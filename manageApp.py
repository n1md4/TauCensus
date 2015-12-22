#!/usr/bin/env python

from flask.ext.script import Manager, Shell, Server
from TauCensus import app

manager = Manager(app)

@manager.command
def createdb():
    from TauCensus.models import db
    db.create_all()

manager.run()
