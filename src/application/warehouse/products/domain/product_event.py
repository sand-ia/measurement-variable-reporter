from datetime import datetime
from uuid import UUID, uuid4
from src.application.shared.entities.domain.aggregate_root import AggregateRoot
from src.application.shared.events.domain.event import Event, EventFactory


class ProductCreatedEvent(Event):
    def __init__(
        self,
        aggregate: AggregateRoot,
        stock: int,
        event_uuid: UUID,
        created_at: datetime,
    ) -> None:
        super().__init__(aggregate, event_uuid, created_at)
        self.stock = stock


class ProductCreatedEventFactory(EventFactory):
    @staticmethod
    def create(
        aggregate: AggregateRoot,
        stock: int,
    ) -> ProductCreatedEvent:
        event_uuid = uuid4()
        created_at = datetime.utcnow()
        event = ProductCreatedEvent(aggregate, stock, event_uuid, created_at)
        return event
