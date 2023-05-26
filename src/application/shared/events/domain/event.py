from datetime import datetime
from typing import Callable, Type, TypeVar
from uuid import UUID, uuid4

from src.application.shared.entities.domain.aggregate_root import AggregateRoot


class Event:
    def __init__(
        self,
        aggregate_root_uuid: UUID,
        event_uuid: UUID | None = None,
        created_at: datetime | None = None,
    ) -> None:
        self.aggregate_root_uuid = aggregate_root_uuid
        self.event_uuid = event_uuid if event_uuid is not None else uuid4()
        self.event_name = self.__class__.__name__
        self.created_at = created_at if created_at is not None else datetime.utcnow()

    @staticmethod
    def get_aggregate_root() -> Type[AggregateRoot]:
        return AggregateRoot


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
