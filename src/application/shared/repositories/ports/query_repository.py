from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar
from uuid import UUID

T = TypeVar("T")


class QueryRepository(Generic[T], ABC):
    @abstractmethod
    def get(self, uuid: UUID) -> T:
        raise NotImplementedError

    @abstractmethod
    def find(self, uuids: List[UUID] | None = None) -> List[T]:
        raise NotImplementedError
