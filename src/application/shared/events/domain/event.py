from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Type, TypeVar
from uuid import UUID

from src.application.shared.entities.domain.aggregate_root import AggregateRoot


@dataclass
class Event:
    aggregate_root_uuid: UUID
    event_uuid: UUID
    created_at: datetime

    @staticmethod
    def get_aggregate_root() -> Type[AggregateRoot]:  # type: ignore
        pass


T = TypeVar("T", bound=Type[Event])


def set_aggregate(aggregate: Type[AggregateRoot]) -> Callable[[T], T]:
    def decorator(cls: T) -> T:
        def get_aggregate_root():
            return aggregate

        cls.get_aggregate_root = get_aggregate_root
        return cls

    return decorator


class EventFactory:
    pass
