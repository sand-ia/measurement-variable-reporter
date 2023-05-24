from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4
from typing import Tuple, Type

from src.application.shared.events.domain.event import Event
from src.application.shared.entities.domain.bounded_context import (
    BoundedContext,
    Warehouse,
)
from src.application.shared.entities.domain.aggregate_root import (
    AggregateRoot,
)
from src.application.shared.entities.domain.aggregate_factory import AggregateFactory


@dataclass
class ProductEvent(Event):
    @staticmethod
    def get_aggregate() -> Type[AggregateRoot]:
        return Product


@dataclass
class ProductCreatedEvent(ProductEvent):
    stock: int


@dataclass
class Product(AggregateRoot):
    stock: int

    @staticmethod
    def get_bounded_context() -> Type[BoundedContext]:
        return Warehouse


class ProductFactory(AggregateFactory):
    @staticmethod
    def create(stock: int) -> Tuple[Product, ProductCreatedEvent]:
        product_uuid = uuid4()
        product = Product(product_uuid, stock)
        event_uuid = uuid4()
        created_at = datetime.utcnow()
        event = ProductCreatedEvent(product_uuid, event_uuid, created_at, stock)
        return product, event
