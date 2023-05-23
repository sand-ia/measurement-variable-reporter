from datetime import datetime
from uuid import UUID
from src.application.shared.entities.domain.aggregate_root import AggregateRoot
from src.application.shared.events.domain.event import Event


class ProductCreatedEvent(Event):
    def __init__(
        self,
        aggregate: AggregateRoot,
        stock: int,
        event_uuid: UUID | None = None,
        created_at: datetime | None = None,
    ) -> None:
        super().__init__(aggregate, event_uuid, created_at)
        self.stock = stock
