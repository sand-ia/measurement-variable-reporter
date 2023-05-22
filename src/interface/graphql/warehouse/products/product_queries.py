from injectable import autowired, Autowired
from graphene import (
    ObjectType,
    ID,
    Int,
    Field,
    ResolveInfo,
)

from src.application.shared.queries.domain.response import Response
from src.application.shared.queries.ports.query_bus import QueryBus
from src.application.warehouse.products.services.get_product_stock.get_product_stock_query import (
    GetProductQuery,
)


AutowiredQueryBus = Autowired(QueryBus)


# class GetProductInput(InputObjectType):
#     uuid = ID()


class GetProductOutput(ObjectType):
    uuid = ID()
    stock = Int()


class ProductQueries(ObjectType):
    get_product = Field(GetProductOutput, uuid=ID())

    @staticmethod
    @autowired
    def resolve_get_product(
        _parent: None,
        _info: ResolveInfo,
        uuid: str,
        query_bus: AutowiredQueryBus,
    ) -> Response:
        get_product_query = GetProductQuery(uuid)
        get_product_response = query_bus.dispatch(get_product_query)
        return get_product_response


# TODO: Handle General Exception