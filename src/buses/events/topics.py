from typing import Dict, Type

from src.application.shared.entities.domain.aggregate_root import AggregateRoot
from src.application.warehouse.products.domain.product import (
    Product as WarehouseProduct,
)

ORGANISATION = "sandia"
SERVICE = "demo"


def _topic_generator(aggregate_root: Type[AggregateRoot]):
    return (
        f"{ORGANISATION}.{SERVICE}."
        f"{aggregate_root.get_bounded_context().__name__.lower()}."
        f"{aggregate_root.__name__.lower()}"
    )


TOPIC: Dict[Type[AggregateRoot], str] = {
    WarehouseProduct: _topic_generator(WarehouseProduct)
}
