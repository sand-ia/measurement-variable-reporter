from typing import Dict, Type

from src.application.shared.entities.domain.aggregate_root import AggregateRoot

from src.application.shared.entities.domain.bounded_context import (
    BoundedContext,
    Warehouse,
)


from src.application.warehouse.products.domain.product import Product

ORGANISATION = "sandia"
SERVICE = "demo"


def _topic_generator(
    bounded_context: Type[BoundedContext], aggregate: Type[AggregateRoot]
):
    return (
        f"{ORGANISATION}.{SERVICE}."
        f"{bounded_context.__name__.lower()}."
        f"{aggregate.__name__.lower()}"
    )


TOPIC: Dict[Type[BoundedContext], Dict[Type[AggregateRoot], str]] = {
    Warehouse: {Product: _topic_generator(Warehouse, Product)}
}
