from graphene import Schema

from src.interface.graphql.warehouse.provider import WarehouseCommands, WarehouseQueries


class Queries(WarehouseQueries):
    pass


class Commands(WarehouseCommands):
    pass


schema = Schema(query=Queries, mutation=Commands)
