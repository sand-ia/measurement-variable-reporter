from uuid import uuid4, UUID
from typing import Tuple

from src.application.warehouse.products.domain.product_event import (
    ProductCreatedEvent,
    ProductCreatedEventFactory,
)
from src.application.shared.entities.domain.aggregate_root import (
    AggregateRoot,
    AggregateFactory,
)


class Product(AggregateRoot):
    def __init__(self, uuid: UUID, stock: int) -> None:
        super().__init__(uuid)
        self.stock = stock


class ProductFactory(AggregateFactory):
    @staticmethod
    def create(stock: int) -> Tuple[Product, ProductCreatedEvent]:
        product_uuid = uuid4()
        product = Product(product_uuid, stock)
        event = ProductCreatedEventFactory.create(product, stock)
        return product, event
