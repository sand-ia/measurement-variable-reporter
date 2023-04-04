from graphene import Schema

from src.measurement_variable_reporter.interface.graphql.queries.query import (
    SampleQuery,
)


class Query(SampleQuery):
    pass


schema = Schema(query=Query)
