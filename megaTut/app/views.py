from flask import render_template
from app import app #import app variable defined in init

@app.route('/')
@app.route('/index')
def index():
	user={'nickname': 'shinchan'} #fake user
	posts = [ #fake array of post
		{
			'author': {'nickname': 'shintest2'},
			'body': 'I made rice cake today!'
		},
		{
			'author': {'nickname': 'harrytest2'},
			'body': 'existential crisis.'
		}
	]
	return render_template('index.html',user=user,posts=posts)
