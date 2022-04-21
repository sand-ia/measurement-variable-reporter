"""Fantastic Brocolli startup."""
from dotenv import load_dotenv
from flask import Flask

# Load enviroment variables
load_dotenv()


def create_app() -> Flask:
    """Start Flask Application.

    :return: Flask Application.
    :rtype: Flask
    """
    app: Flask = Flask(__name__)

    # Start DB Connection

    # Start Controllers

    # Start Dependency Injections

    # Start Broker Consumers

    return app
