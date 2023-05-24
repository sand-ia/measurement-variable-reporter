from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4
from typing import Tuple

from src.application.shared.events.domain.event import Event, set_aggregate
from src.application.warehouse.context import WarehouseAggregateRoot
from src.application.shared.entities.domain.aggregate_factory import AggregateFactory
from src.buses.events.topics import topify


@topify
@dataclass
class Product(WarehouseAggregateRoot):
    stock: int

    def say_hi(self) -> Event:
        print("Hi! 👋")
        event_uuid = uuid4()
        created_at = datetime.utcnow()
        event = ProductSayHiEvent(self.uuid, event_uuid, created_at)
        return event


class ProductFactory(AggregateFactory):
    @staticmethod
    def create(stock: int) -> Tuple[Product, Event]:
        product_uuid = uuid4()
        product = Product(product_uuid, stock)
        event_uuid = uuid4()
        created_at = datetime.utcnow()
        event = ProductCreatedEvent(product_uuid, event_uuid, created_at, stock)
        return product, event


@set_aggregate(Product)
class ProductEvent(Event):
    pass


@dataclass
class ProductCreatedEvent(ProductEvent):
    stock: int


@dataclass
class ProductSayHiEvent(ProductEvent):
    pass
