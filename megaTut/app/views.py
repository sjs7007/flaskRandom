from app import app #import app variable defined in init

@app.route('/')
@app.route('/index')
def index():
	return "<h1>Hello, World!</h1>"

