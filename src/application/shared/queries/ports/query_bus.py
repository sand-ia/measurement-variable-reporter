from abc import ABC, abstractmethod

from src.application.shared.queries.domain.query import Query
from src.application.shared.queries.domain.response import Response


class QueryBus(ABC):
    # * When implementing this class, register all the QueryHandler
    # * in the __init__.

    @abstractmethod
    def dispatch(self, query: Query) -> Response:
        raise NotImplementedError
