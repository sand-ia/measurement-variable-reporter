import json
from typing import Any, Dict, Type, TypeAlias
from injectable import injectable, autowired, Autowired

from src.shared.events.domain.event_handler import (
    EventHandler,
    set_aggregate,
)
from src.application.warehouse.products.domain.product import (
    Product,
    ProductCreatedEvent,
    ProductReceivedEvent,
    ProductShippedEvent,
)
from src.application.warehouse.products.ports.product_query_respository import (
    ProductQueryRepository,
)
from src.application.warehouse.products.ports.product_command_repository import (
    ProductCommandRepository,
)

DefaultProductQueryRepository: TypeAlias = ProductQueryRepository
AutowiredProductQueryRepository: Type[DefaultProductQueryRepository] = Autowired(
    DefaultProductQueryRepository
)  # type: ignore
DefaultProductCommandRepository: TypeAlias = ProductCommandRepository
AutowiredProductCommandRepository: Type[DefaultProductCommandRepository] = Autowired(
    DefaultProductCommandRepository
)  # type: ignore


@set_aggregate(Product)
@injectable(singleton=True)  # type: ignore
class ProductEventHandler(EventHandler):
    @autowired
    def __init__(
        self,
        product_query_repository: AutowiredProductQueryRepository,
        product_command_repository: AutowiredProductCommandRepository,
    ) -> None:
        self._product_query_repository = product_query_repository
        self._product_command_repository = product_command_repository
        self.switcher = {
            ProductCreatedEvent.__name__: self.handle_product_create_event,
            ProductReceivedEvent.__name__: self.handle_product_received_event,
            ProductShippedEvent.__name__: self.handle_product_shipped_event,
        }

    def handle(self, event: str) -> None:
        # TODO: Handle error if doesnt match event type
        event_dict: Dict[str, Any] = json.loads(event)
        event_uuid: str = event_dict["uuid"]
        event_name: str = event_dict["name"]

        print(f"Consumer[Product]: Consuming event {event_uuid}")

        handle = self.switcher.get(event_name)
        if handle is not None:
            print(f"Consumer[Product]: Event match with type {event_name}")
            handle(event_dict)

    def handle_product_create_event(self, event: Dict[str, Any]):
        product_dict: Dict[str, Any] = event["product"]
        product = Product(**product_dict)
        self._product_command_repository.save(product)

    def handle_product_received_event(self, event: Dict[str, Any]):
        product_uuid = event["aggregate_root_uuid"]
        product = self._product_query_repository.get(product_uuid)
        amount: int = event["amount"]
        new_stock = product.stock + amount
        updates = {"stock": new_stock}
        self._product_command_repository.update(product.uuid, updates)

    def handle_product_shipped_event(self, event: Dict[str, Any]):
        product_uuid = event["aggregate_root_uuid"]
        product = self._product_query_repository.get(product_uuid)
        amount: int = event["amount"]
        new_stock = product.stock - amount
        updates = {"stock": new_stock}
        self._product_command_repository.update(product.uuid, updates)
