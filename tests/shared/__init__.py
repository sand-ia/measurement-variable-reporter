"""Fantastic Brocolli startup."""
from flask import Flask
from flask_graphql import GraphQLView
from injectable import load_injection_container
from src.warehouse.interface.graphql.schema import schema


def create_app() -> Flask:
    # Instantiate Flask object.
    app = Flask(__name__)

    # Load injection Container.
    load_injection_container()

    # Create GraphQL view with required dependencies injected.
    graphql_view = GraphQLView.as_view("graphql", schema=schema)

    # Add GraphQL controller to Flask app.
    app.add_url_rule("/graphql", view_func=graphql_view)

    # TODO: Start Broker Consumers

    return app
