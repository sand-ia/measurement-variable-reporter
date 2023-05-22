from dataclasses import dataclass
from uuid import UUID
from src.application.shared.queries.domain.query import Query


@dataclass
class GetProductQuery(Query):
    uuid: UUID
