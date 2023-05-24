from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type
from src.application.shared.entities.domain.bounded_context import BoundedContext
from src.application.shared.entities.domain.entity import Entity


@dataclass
class AggregateRoot(Entity, ABC):
    @staticmethod
    @abstractmethod
    def get_bounded_context() -> Type[BoundedContext]:
        raise NotImplementedError


class AggregateFactory:
    pass
