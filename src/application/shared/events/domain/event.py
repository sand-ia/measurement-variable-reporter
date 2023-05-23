from datetime import datetime
from uuid import UUID, uuid4

from src.application.shared.entities.domain.aggregate_root import AggregateRoot


class Event:
    def __init__(
        self,
        aggregate: AggregateRoot,
        event_uuid: UUID | None = None,
        created_at: datetime | None = None,
    ) -> None:
        self.aggregate_uuid = aggregate.uuid
        self.aggregate = aggregate.__class__
        self.event_uuid = event_uuid if event_uuid is not None else str(uuid4())
        self.event = self.__class__
        self.created_at = created_at if created_at is not None else datetime.utcnow()
