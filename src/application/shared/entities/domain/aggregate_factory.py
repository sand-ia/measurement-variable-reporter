from abc import ABC, abstractmethod
from typing import Tuple

from src.application.shared.entities.domain.aggregate_root import AggregateRoot
from src.application.shared.events.domain.event import Event


class AggregateFactory(ABC):
    @staticmethod
    @abstractmethod
    def create() -> Tuple[AggregateRoot, Event]:
        raise NotImplementedError
