from typing import Any, Type, TypeAlias
from injectable import injectable, autowired, Autowired

from src.application.shared.events.domain.event_handler import (
    EventHandler,
    set_aggregate,
)
from src.application.warehouse.products.domain.product import (
    Product,
    ProductCreatedEvent,
    ProductShipEvent,
)
from src.application.warehouse.products.ports.product_respository import (
    ProductRepository,
)

DefaultProductRepository: TypeAlias = ProductRepository
AutowiredProductRepository: Type[DefaultProductRepository] = Autowired(
    DefaultProductRepository
)  # type: ignore


@set_aggregate(Product)
@injectable(singleton=True)  # type: ignore
class ProductEventHandler(EventHandler):
    @autowired
    def __init__(self, product_repository: AutowiredProductRepository) -> None:
        self._product_repository = product_repository
        self.switcher = {
            ProductCreatedEvent.__name__: self.handle_product_create_event,
            ProductShipEvent.__name__: self.handle_say_hi_event,
        }

    def handle(self, event: Any) -> None:
        # TODO: Handle error if doesnt match event type
        event_uuid = event.uuid
        event_name = event.name

        print(f"Consumer[Product]: Consuming event {event_uuid}")

        handler = self.switcher.get(event_name)
        if handler is not None:
            handler(event)

    def handle_product_create_event(self, event: Any):
        print(f"Consumer[Product]: Event match with type {event.name}")

    def handle_say_hi_event(self, event: Any):
        print(f"Consumer[Product]: Event match with type {event.name}")
