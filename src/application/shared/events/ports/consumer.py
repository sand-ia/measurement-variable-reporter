from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from src.application.shared.events.domain.event import Event

E = TypeVar("E", bound=Event)


class Consumer(Generic[E], ABC):
    @abstractmethod
    def subscribe(self, topic: str, callback: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def subscribe_and_wait(self, topic: str) -> Any:
        raise NotImplementedError
