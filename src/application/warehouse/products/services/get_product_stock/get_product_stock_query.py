from dataclasses import dataclass
from src.application.shared.queries.domain.query import Query


@dataclass
class GetProductQuery(Query):
    uuid: str
