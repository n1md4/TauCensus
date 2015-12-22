from flask_sqlalchemy import SQLAlchemy
from  FlaskApp import app

db = SQLAlchemy(app)

class Tau(db.Model):
	__tablename__ = 'cadres'
	id = db.Column(db.Integer, primary_key=True)
	designation = db.Column(db.String(300))
	location = db.Column(db.String(300)) 
	founding = db.Column(db.String(1000)) 
	commanding = db.Column(db.String(500))
	c_status = db.Column(db.String(1000))
	c_location = db.Column(db.String(300))
	mission = db.Column(db.String(1200))

	def __init__(self, designation, location, founding, commanding, c_status, c_location, mission):
		self.designation = designation
		self.location = location
		self.founding = founding
		self.commanding = commanding
		self.c_status = c_status
		self.c_location = c_location
		self.mission = mission

	def __repr__(self):
		return '<Tau %r>' % self.id
