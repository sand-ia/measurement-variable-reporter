from src.shared.repositories.ports.query_repository import QueryRepository
from src.application.warehouse.products.projections.product_current_state import (
    ProductCurrentState,
)


class ProductQueryRepository(QueryRepository[ProductCurrentState]):
    pass
