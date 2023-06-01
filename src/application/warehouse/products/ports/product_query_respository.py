from src.shared.repositories.ports.query_repository import QueryRepository
from src.application.warehouse.products.domain.product import Product


class ProductQueryRepository(QueryRepository[Product]):
    pass
