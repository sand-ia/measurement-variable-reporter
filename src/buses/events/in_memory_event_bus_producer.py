from injectable import injectable

from src.application.shared.events.domain.event import Event
from src.application.shared.events.ports.producer import Producer
from src.buses.events.in_memory_event_bus import BusEvent, in_memory_event_bus
from src.buses.events.topics import TOPIC


@injectable(singleton=True)  # type: ignore
class InMemoryEventBusProducer(Producer):
    def publish(self, event: Event) -> None:
        aggregate_root = event.__class__.get_aggregate_root()
        topic = TOPIC.get(aggregate_root)
        if topic is None:
            raise NotImplementedError(
                f"InMemoryEventBusProducer: No topic found for this aggregate root {aggregate_root}"
            )
        bus_event = BusEvent(event)
        in_memory_event_bus.publish(topic, bus_event)
