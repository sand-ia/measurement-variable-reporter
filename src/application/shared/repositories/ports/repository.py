from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar, Union
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
    def update(self, uuid: UUID, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, uuid: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def find(self, uuids: Union[List[UUID], None] = None) -> List[T]:
        raise NotImplementedError
