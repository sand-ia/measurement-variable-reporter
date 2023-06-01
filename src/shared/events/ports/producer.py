from abc import ABC, abstractmethod

from src.shared.events.domain.event import Event


class Producer(ABC):
    @abstractmethod
    def publish(self, event: Event) -> None:
        raise NotImplementedError
