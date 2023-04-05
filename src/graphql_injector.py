from typing import Any, Callable, List
from injector import Binder, Injector
from flask_graphql import GraphQLView
from graphene import Schema

_ModuleT = Callable[[Binder], None]


def create_injected_graphql_view(schema: Schema, modules: List[_ModuleT] = []) -> Any:
    injector = Injector()
    installed_injector = _install_modules(injector, modules)
    graphql_view = _get_graphql_view(installed_injector, schema)
    return graphql_view


def _install_modules(injector: Injector, modules: List[_ModuleT] = []) -> Injector:
    for module in modules:
        injector.binder.install(module)
    return injector


def _get_graphql_view(injector: Injector, schema: Schema) -> Any:
    graphql_view: Any = GraphQLView.as_view(
        "graphql", schema=schema, get_context=lambda: {"dependency_container": injector}
    )
    return graphql_view
