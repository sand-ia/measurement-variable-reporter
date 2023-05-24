from datetime import datetime
from uuid import UUID
from typing import Tuple

from src.application.shared.events.domain.event import Event, set_aggregate
from src.application.warehouse.context import WarehouseAggregateRoot
from src.buses.events.topics import topify


@topify
class Product(WarehouseAggregateRoot):
    def __init__(self, stock: int, uuid: UUID | None = None) -> None:
        super().__init__(uuid)
        self.stock = stock

    def say_hi(self) -> Event:
        print("Hi! 👋")
        event = ProductSayHiEvent(self.uuid)
        return event


class ProductFactory:
    @staticmethod
    def create(stock: int) -> Tuple[Product, Event]:
        product = Product(stock)
        event = ProductCreatedEvent(product.uuid, stock)
        return product, event


@set_aggregate(Product)
class ProductEvent(Event):
    pass


class ProductCreatedEvent(ProductEvent):
    def __init__(
        self,
        aggregate_root_uuid: UUID,
        stock: int,
        event_uuid: UUID | None = None,
        created_at: datetime | None = None,
    ) -> None:
        super().__init__(aggregate_root_uuid, event_uuid, created_at)
        self.stock = stock


class ProductSayHiEvent(ProductEvent):
    pass
