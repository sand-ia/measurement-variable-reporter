from abc import ABC, abstractmethod

from src.application.shared.events.domain.event import Event


class Producer(ABC):
    @abstractmethod
    def publish(self, topic: str, event: Event) -> None:
        raise NotImplementedError
