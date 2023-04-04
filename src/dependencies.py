"""Configure the dependency injection tree."""
from injector import singleton

# Ports
from src.measurement_variable_reporter.application.services.testService import (
    TestService,
)


# Adapters
from src.measurement_variable_reporter.application.services.impl.testServiceDefault import (
    TestServiceDefault,
)


def configure(binder):
    binder.bind(TestService, to=TestServiceDefault, scope=singleton)
