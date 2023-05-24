from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Type
from uuid import UUID

from src.application.shared.entities.domain.aggregate_root import AggregateRoot


@dataclass
class Event(ABC):
    aggregate_uuid: UUID
    event_uuid: UUID
    created_at: datetime

    @staticmethod
    @abstractmethod
    def get_aggregate() -> Type[AggregateRoot]:
        raise NotImplementedError


class EventFactory:
    pass
