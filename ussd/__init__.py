""" make sure to go through the readme file for further explanation """

from flask import Flask
from ussd.ussd import ussd

def create_app():
    app = Flask(__name__)

    app.register_blueprint(ussd)
    return app