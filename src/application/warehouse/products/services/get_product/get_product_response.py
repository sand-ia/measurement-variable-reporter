from dataclasses import dataclass
from src.application.shared.queries.domain.response import Response


@dataclass
class GetProductResponse(Response):
    uuid: str
    stock: int
