"""Fantastic Brocolli startup."""
from flask import Flask
from flask_graphql import GraphQLView
from flask_injector import FlaskInjector

from src.dependencies import configure
from src.measurement_variable_reporter.interface.graphql.schema import schema


def create_app() -> Flask:
    """Start Flask Application.

    :return: Flask Application.
    :rtype: Flask
    """
    app: Flask = Flask(__name__)

    # Start DB Connection

    # Start Controllers
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )

    # Start Dependency Injections

    # Start Broker Consumers

    return app
