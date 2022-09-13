"""Fantastic Brocolli startup."""
from flask import Flask
from src.measurement_variable_reporter.interface.controllers.graphql_controller import (
    graphql_controller,
)


def create_app() -> Flask:
    """Start Flask Application.

    :return: Flask Application.
    :rtype: Flask
    """
    app: Flask = Flask(__name__)

    # Start DB Connection

    # Start Controllers
    app.register_blueprint(graphql_controller)

    # Start Dependency Injections

    # Start Broker Consumers

    return app
