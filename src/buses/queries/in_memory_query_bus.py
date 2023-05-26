from typing import Dict, List, Type, TypeAlias
from inspect import signature
from injectable import Autowired, autowired, injectable
from src.application.shared.queries.domain.query import Query
from src.application.shared.queries.domain.response import Response
from src.application.shared.queries.ports.query_bus import QueryBus
from src.application.shared.queries.domain.query_handler import QueryHandler

DefaultQueryHandler: TypeAlias = QueryHandler[Query, Response]
QueryHandlers: TypeAlias = List[DefaultQueryHandler]
AutowiredQueryHandlers: Type[QueryHandlers] = Autowired(QueryHandlers)  # type: ignore


@injectable(singleton=True)  # type: ignore
class InMemoryQueryBus(QueryBus):
    @autowired
    def __init__(self, query_handlers: AutowiredQueryHandlers) -> None:
        self.query_handlers: Dict[type, DefaultQueryHandler] = {}
        for query_handler in query_handlers:
            handle = query_handler.handle
            parameters = signature(handle).parameters.values()
            parameter = list(parameters)[0]
            query_class = parameter.annotation
            self.query_handlers[query_class] = query_handler

    def dispatch(self, query: Query) -> Response:
        query_class = query.__class__
        handler = self.query_handlers.get(query_class)
        if handler is None:
            # TODO: raise correct exception.
            raise Exception("No handler registered")
        return handler.handle(query)
