from flask import Flask, render_template
from models import *
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://tau:kuhohNg3@localhost/tau_census'

@app.route("/Database/")
def Database():
	return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)
