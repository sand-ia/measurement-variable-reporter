from typing import Tuple
from uuid import UUID, uuid4
from src.application.shared.entities.domain.aggregate_root import AggregateRoot
from src.application.warehouse.products.domain.product_event import ProductCreatedEvent


class Product(AggregateRoot):
    def __init__(self, uuid: UUID, stock: int) -> None:
        super().__init__(uuid)
        self.stock = stock


class ProductFactory:
    @staticmethod
    def create(stock: int) -> Tuple[Product, ProductCreatedEvent]:
        uuid = uuid4()
        product = Product(uuid, stock)
        event = ProductCreatedEvent(uuid, product)
        return product, event
