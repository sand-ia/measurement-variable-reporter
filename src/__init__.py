"""Fantastic Brocolli startup."""
from flask import Flask
from src.dependencies import configure_graphql_injector
from src.graphql_injector import create_injected_graphql_view
from src.measurement_variable_reporter.interface.graphql.schema import schema


def create_app() -> Flask:
    # Instantiate Flask object.
    app = Flask(__name__)

    # Create GraphQL view with required dependencies injected.
    graphql_view = create_injected_graphql_view(schema, [configure_graphql_injector])

    # Add GraphQL controller to Flask app.
    app.add_url_rule("/graphql", view_func=graphql_view)

    # Start Broker Consumers

    return app
