from datetime import datetime
from uuid import UUID
from typing import Tuple

from src.application.shared.events.domain.event import Event, set_aggregate
from src.application.warehouse.context import WarehouseAggregateRoot
from src.buses.events.topics import topify


@topify
class Product(WarehouseAggregateRoot):
    def __init__(self, name: str, stock: int, uuid: UUID | None = None) -> None:
        super().__init__(uuid)
        self.name = name
        self.stock = stock

    def ship(self, amount: int) -> Event:
        if self.stock < amount:
            raise Exception(f"Not enought stock to ship product {str(self.uuid)}")
        self.stock -= amount
        event = ProductShipEvent(self)
        return event


class ProductFactory:
    @staticmethod
    def create(name: str, stock: int) -> Tuple[Product, Event]:
        product = Product(name, stock)
        event = ProductCreatedEvent(product)
        return product, event


@set_aggregate(Product)
class ProductEvent(Event):
    pass


class ProductCreatedEvent(ProductEvent):
    def __init__(
        self,
        product: Product,
        event_uuid: UUID | None = None,
        created_at: datetime | None = None,
    ) -> None:
        super().__init__(product.uuid, event_uuid, created_at)
        self.product = product


class ProductShipEvent(ProductEvent):
    def __init__(
        self,
        product: Product,
        event_uuid: UUID | None = None,
        created_at: datetime | None = None,
    ) -> None:
        super().__init__(product.uuid, event_uuid, created_at)
        self.new_stock = product.stock
