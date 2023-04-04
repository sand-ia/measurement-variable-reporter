from abc import ABC, abstractmethod


class TestService(ABC):
    @abstractmethod
    def create(self, name: str) -> None:
        raise NotImplementedError
