from injectable import injectable

from src.application.shared.queries.domain.query_handler import QueryHandler
from src.application.warehouse.products.services.get_product_stock.get_product_stock_query import (
    GetProductQuery,
)
from src.application.warehouse.products.services.get_product_stock.product_stock_response import (
    GetProductResponse,
)


@injectable(singleton=True)  # type: ignore
class GetProductStockQueryHandler(QueryHandler[GetProductQuery, GetProductResponse]):
    def handle(self, query: GetProductQuery) -> GetProductResponse:
        return GetProductResponse("1234", 5)
