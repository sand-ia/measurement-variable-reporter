from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, TypeVar
from uuid import UUID

from src.shared.entities.domain.projection import Projection

T = TypeVar("T", bound=Projection)


class CommandRepository(Generic[T], ABC):
    @abstractmethod
    def save(self, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, uuid: UUID, updates: Dict[str, Any]) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, uuid: UUID) -> None:
        raise NotImplementedError
