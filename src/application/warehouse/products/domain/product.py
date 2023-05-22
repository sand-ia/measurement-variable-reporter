from uuid import uuid4
from src.application.shared.entities.domain.aggregate_root import AggregateRoot
from src.application.warehouse.products.domain.product_event import ProductCreatedEvent


class Product(AggregateRoot):
    def __init__(self, uuid: str, stock: int) -> None:
        self.uuid = uuid
        self.stock = stock


class ProductFactory:
    @staticmethod
    def create(stock: int):
        uuid = str(uuid4())
        product = Product(uuid, stock)
        event = ProductCreatedEvent(uuid, product)
        return product, event
