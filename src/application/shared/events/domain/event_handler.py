from abc import ABC, abstractmethod
from typing import Callable, Type, TypeVar

from src.application.shared.entities.domain.aggregate_root import AggregateRoot
from src.application.shared.events.domain.event import Event


class EventHandler(ABC):
    @abstractmethod
    def handle(self, event: Event) -> None:
        raise NotImplementedError

    @staticmethod
    def get_aggregate_root() -> Type[AggregateRoot]:
        return AggregateRoot


T = TypeVar("T", bound=Type[EventHandler])


def set_aggregate(aggregate: Type[AggregateRoot]) -> Callable[[T], T]:
    def decorator(cls: T) -> T:
        def get_aggregate_root():
            return aggregate

        cls.get_aggregate_root = get_aggregate_root
        return cls

    return decorator