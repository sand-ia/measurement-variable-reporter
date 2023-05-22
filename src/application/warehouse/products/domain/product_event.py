from datetime import datetime
from typing import Any, Union
from uuid import UUID
from src.application.shared.events.domain.event import Event
from src.application.warehouse.aggregates import WarehouseAggregate


class ProductEvent(Event):
    def __init__(
        self,
        aggregate_uuid: UUID,
        data: Any,
        event_uuid: Union[UUID, None] = None,
        created_at: Union[datetime, None] = None,
    ) -> None:
        super().__init__(
            aggregate_uuid,
            WarehouseAggregate.PRODUCT,
            data,
            event_uuid,
            created_at,
        )


class ProductCreatedEvent(ProductEvent):
    pass
