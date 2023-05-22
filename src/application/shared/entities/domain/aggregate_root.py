from abc import ABC

from src.application.shared.entities.domain.entity import Entity


class AggregateRoot(Entity, ABC):
    pass
