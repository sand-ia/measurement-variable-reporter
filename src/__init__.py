"""Fantastic Brocolli startup."""
from flask import Flask


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
