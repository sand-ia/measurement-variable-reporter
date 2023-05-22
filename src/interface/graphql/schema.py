from graphene import Schema

from src.interface.graphql.warehouse.provider import WarehouseQueries


class Queries(WarehouseQueries):
    pass


schema = Schema(query=Queries)
