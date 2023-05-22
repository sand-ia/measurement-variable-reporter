from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.application.shared.queries.domain.query import Query
from src.application.shared.queries.domain.response import Response

Q = TypeVar("Q", bound=Query)
R = TypeVar("R", bound=Response)


class QueryHandler(Generic[Q, R], ABC):
    @abstractmethod
    def handle(self, query: Q) -> R:
        raise NotImplementedError
