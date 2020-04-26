from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config):
	app = Flask(__name__)

	# Initializing flask extensions
	bootstrap.init_app(app)

	return app