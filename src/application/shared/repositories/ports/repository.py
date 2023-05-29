from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar
from uuid import UUID

T = TypeVar("T")


class Repository(Generic[T], ABC):
    @abstractmethod
    def save(self, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, uuid: UUID) -> T:
        raise NotImplementedError

    @abstractmethod
    def update(self, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, uuid: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def find(self, uuids: List[UUID] | None = None) -> List[T]:
        raise NotImplementedError
