"""Configure the dependency injection tree."""
from injector import Binder, singleton

# Ports
from src.measurement_variable_reporter.application.services.testService import (
    TestService,
)


# Adapters
from src.measurement_variable_reporter.application.services.impl.testServiceDefault import (
    TestServiceDefault,
)


def configure_graphql_injector(binder: Binder) -> None:
    binder.bind(TestService, to=TestServiceDefault, scope=singleton)
