from app import app #import app variable defined in init

@app.route('/')
@app.route('/index')
def index():
	user={'nickname': 'shinchan'} #fake user
	return '''
<html>
	<head>
		<title>Home Page</title>
	</head>
	<body>
		<h3>Hello, ''' + user['nickname'] + '''</h3>
	</body>
</html>
	'''

