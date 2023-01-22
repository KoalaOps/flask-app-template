from flask import Flask


app = Flask(__name__)

# Load Configuration of application. Check configuration.py for more details
app.config.from_object('app.configuration.DevConfig')


from app import routes
