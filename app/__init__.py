from flask import Flask
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics


app = Flask(__name__)

# Prometheus Metrics
# Using example from https://github.com/rycus86/prometheus_flask_exporter/tree/master/examples/gunicorn
metrics = GunicornPrometheusMetrics(app)

with open("VERSION", "rb") as f:
		image_ver = f.read().decode("utf-8")
		metrics.info('app_info', 'Application info', version=image_ver)

# Load Configuration of application. Check configuration.py for more details
app.config.from_object('app.configuration.DevConfig')


from app import routes
