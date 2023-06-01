from dataclasses import dataclass
from uuid import UUID
from src.shared.queries.domain.response import Response


@dataclass
class GetProductResponse(Response):
    uuid: UUID
    stock: int
