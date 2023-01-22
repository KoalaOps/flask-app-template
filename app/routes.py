from app import app


@app.route('/')
def index():
	return "hello world!"


@app.route('/koala')
def koala():
	return "Hello world! (%s v%s)" % (app.config['SERVICE_NAME'], app.config['VERSION'])
	
