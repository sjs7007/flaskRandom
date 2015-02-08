from flask import render_template
from app import app #import app variable defined in init

@app.route('/')
@app.route('/index')
def index():
	user={'nickname': 'shinchan'} #fake user
	return render_template('index.html',user=user)
