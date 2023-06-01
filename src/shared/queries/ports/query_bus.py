from abc import ABC, abstractmethod

from src.shared.queries.domain.query import Query
from src.shared.queries.domain.response import Response


class QueryBus(ABC):
    # * When implementing, register all the query handlers in the constructor.

    @abstractmethod
    def dispatch(self, query: Query) -> Response:
        raise NotImplementedError
