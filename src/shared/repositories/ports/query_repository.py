from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar
from uuid import UUID

from src.shared.entities.domain.projection import Projection

T = TypeVar("T", bound=Projection)


class QueryRepository(Generic[T], ABC):
    @abstractmethod
    def get(self, uuid: UUID) -> T:
        raise NotImplementedError

    @abstractmethod
    def find(self, uuids: List[UUID] | None = None) -> List[T]:
        raise NotImplementedError
