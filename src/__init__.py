from flask import Flask
from flask_graphql import GraphQLView
from injectable import load_injection_container

from src.buses.events.in_memory_event_bus import in_memory_event_bus
from src.buses.events.in_memory_event_bus_consumer import InMemoryEventBusConsumer

from src.infrastructure.repositories.in_memory_db import in_memory_db
from src.interface.graphql.schema import schema


def create_app() -> Flask:
    # TODO: Add Feature Flags
    app = Flask(__name__)
    load_injection_container()
    load_presentation(app)
    load_infraestructure(app)
    load_buses()
    return app


def load_presentation(app: Flask) -> None:
    # TODO: health check endpoint
    load_graphql(app)


def load_graphql(app: Flask):
    graphql_view = GraphQLView.as_view("graphql", schema=schema)  # type: ignore
    app.add_url_rule("/graphql", view_func=graphql_view)  # type: ignore


def load_infraestructure(_: Flask) -> None:
    # TODO: load_in_memory_database.
    load_in_memory_db()
    # TODO: load_logger


def load_in_memory_db():
    try:
        # TODO: Get user and pass from .env
        in_memory_db.connect(user="sandia", password="sandia")
    except PermissionError as error:
        # TODO: handle error
        print(error)


def load_buses():
    load_in_memory_event_bus()
    load_event_bus_consumers()


def load_in_memory_event_bus():
    try:
        # TODO: Get user and pass from .env
        in_memory_event_bus.connect(user="sandia", password="sandia")
    except PermissionError as error:
        # TODO: handle error
        print(error)


def load_event_bus_consumers():
    InMemoryEventBusConsumer()  # type: ignore pylint: disable=E1120
