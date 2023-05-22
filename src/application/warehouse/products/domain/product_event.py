from datetime import datetime
from typing import Any, Union
from src.application.shared.events.domain.event import Event

AGGREGATE = "product"


class ProductEvent(Event):
    def __init__(
        self,
        aggregate_uuid: str,
        data: Any,
        event_uuid: Union[str, None] = None,
        created_at: Union[datetime, None] = None,
    ) -> None:
        super().__init__(
            aggregate_uuid,
            AGGREGATE,
            data,
            event_uuid,
            created_at,
        )


class ProductCreatedEvent(ProductEvent):
    pass
