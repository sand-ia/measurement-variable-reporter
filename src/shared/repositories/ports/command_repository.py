from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, TypeVar
from uuid import UUID

T = TypeVar("T")


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
