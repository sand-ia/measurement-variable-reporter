from injectable import injectable
from src.application.shared.events.domain.event import Event

from src.application.shared.events.domain.event_handler import (
    EventHandler,
    set_aggregate,
)

from src.application.warehouse.products.domain.product import (
    Product,
    ProductCreatedEvent,
    ProductSayHiEvent,
)


@set_aggregate(Product)
@injectable(singleton=True)  # type: ignore
class ProductEventHandler(EventHandler):
    def handle(self, event: Event) -> None:
        event_uuid = event.uuid
        event_name = event.name
        print(f"Consumer[Product]: Consuming event {event_uuid}")

        if event_name == ProductCreatedEvent.__name__:
            print(f"Consumer[Product]: Event match with type {event_name}")

        if event_name == ProductSayHiEvent.__name__:
            print(f"Consumer[Product]: Event match with type {event_name}")
