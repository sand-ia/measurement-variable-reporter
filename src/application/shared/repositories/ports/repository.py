from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar, Union

T = TypeVar("T")


class Repository(Generic[T], ABC):
    @abstractmethod
    def save(self, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, uuid: str) -> T:
        raise NotImplementedError

    @abstractmethod
    def update(self, uuid: str, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, uuid: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def find(self, uuids: Union[List[str], None] = None) -> List[T]:
        raise NotImplementedError
