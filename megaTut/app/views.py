from flask import render_template, flash, redirect
from app import app #import app variable defined in init
from .forms import LoginForm

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

@app.route('/login', methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',title='Sign In', form=form)
