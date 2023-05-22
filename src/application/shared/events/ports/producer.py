from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.buses import events


M = TypeVar("M", bound=events)


class Producer(Generic[M], ABC):
    @abstractmethod
    def publish(self, topic: str, message: M) -> None:
        raise NotImplementedError
