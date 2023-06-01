from typing import List
from uuid import UUID
from injectable import injectable

from src.application.warehouse.products.projections.product_current_state import (
    ProductCurrentState,
)
from src.application.warehouse.products.ports.product_query_respository import (
    ProductQueryRepository,
)
from src.infrastructure.repositories.in_memory_db import in_memory_db


@injectable(singleton=True)  # type: ignore
class InMemoryDBProductQueryRepository(ProductQueryRepository):
    def get(self, uuid: UUID) -> ProductCurrentState:
        product_dict = in_memory_db.get("products", str(uuid))
        product = ProductCurrentState(**product_dict)
        return product

    def find(self, uuids: List[UUID] | None = None) -> List[ProductCurrentState]:
        raise NotImplementedError
