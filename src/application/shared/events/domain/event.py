from datetime import datetime
from typing import Any, Union
from uuid import UUID, uuid4

from src.application.warehouse.aggregates import WarehouseAggregate


class Event:
    def __init__(
        self,
        aggregate_uuid: UUID,
        aggregate: WarehouseAggregate,
        data: Any,
        event_uuid: Union[UUID, None] = None,
        created_at: Union[datetime, None] = None,
    ) -> None:
        self._event_uuid = event_uuid if event_uuid is not None else str(uuid4())
        self._aggregate_uuid = aggregate_uuid
        self._aggregate = aggregate
        self._data = data
        self._created_at = created_at if created_at is not None else datetime.utcnow()
