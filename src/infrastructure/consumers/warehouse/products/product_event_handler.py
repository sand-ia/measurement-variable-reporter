from injectable import injectable
from src.application.shared.events.domain.event import Event

from src.application.shared.events.domain.event_handler import (
    EventHandler,
    set_aggregate,
)

from src.application.warehouse.products.domain.product import Product


@set_aggregate(Product)
@injectable(singleton=True)  # type: ignore
class ProductEventHandler(EventHandler):
    def handle(self, event: Event) -> None:
        print(f"Consumer[Product]: {event.event_name}")
