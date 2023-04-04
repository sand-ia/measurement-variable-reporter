from src.measurement_variable_reporter.application.services.testService import (
    TestService,
)


class TestServiceDefault(TestService):
    def create(self, name: str) -> None:
        print(name)
