from typing import Type, TypeAlias
from injectable import injectable, autowired, Autowired

from src.shared.queries.domain.query_handler import QueryHandler
from src.application.warehouse.products.services.get_product.get_product_query import (
    GetProductQuery,
)
from src.application.warehouse.products.services.get_product.get_product_response import (
    GetProductResponse,
)
from src.application.warehouse.products.ports.product_query_respository import (
    ProductQueryRepository,
)

DefaultProductQueryRepository: TypeAlias = ProductQueryRepository
AutowiredProductQueryRepository: Type[DefaultProductQueryRepository] = Autowired(
    DefaultProductQueryRepository
)  # type: ignore


@injectable(singleton=True)  # type: ignore
class GetProductQueryHandler(QueryHandler[GetProductQuery, GetProductResponse]):
    @autowired
    def __init__(
        self, product_query_repository: AutowiredProductQueryRepository
    ) -> None:
        self._product_query_repository = product_query_repository

    def handle(self, query: GetProductQuery) -> GetProductResponse:
        uuid = query.uuid
        product = self._product_query_repository.get(uuid)
        get_product_response = GetProductResponse(
            product.uuid,
            product.stock,
        )
        return get_product_response
