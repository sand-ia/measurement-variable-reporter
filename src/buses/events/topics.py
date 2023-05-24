from typing import Dict, Type

from src.application.shared.entities.domain.aggregate_root import AggregateRoot
from src.application.warehouse.products.domain.product import Product

ORGANISATION = "sandia"
SERVICE = "demo"


def _topic_generator(aggregate: Type[AggregateRoot]):
    return (
        f"{ORGANISATION}.{SERVICE}."
        f"{aggregate.get_bounded_context().__name__.lower()}."
        f"{aggregate.__name__.lower()}"
    )


TOPIC: Dict[Type[AggregateRoot], str] = {Product: _topic_generator(Product)}
