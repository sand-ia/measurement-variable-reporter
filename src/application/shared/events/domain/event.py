from datetime import datetime
from uuid import UUID, uuid4

from src.application.shared.entities.domain.aggregate_root import AggregateRoot


class Event:
    def __init__(
        self,
        aggregate: AggregateRoot,
        event_uuid: UUID,
        created_at: datetime,
    ) -> None:
        self.aggregate_uuid = aggregate.uuid
        self.aggregate = aggregate.__class__
        self.event_uuid = event_uuid
        self.event = self.__class__
        self.created_at = created_at


class EventFactory:
    pass
    # @staticmethod
    # def create(aggregate: AggregateRoot) -> Event:
    #     event_uuid = uuid4()
    #     created_at = datetime.utcnow()
    #     event = Event(aggregate, event_uuid, created_at)
    #     return event
