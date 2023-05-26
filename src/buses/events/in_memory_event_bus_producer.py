from injectable import injectable

from src.application.shared.events.domain.event import Event
from src.application.shared.events.ports.producer import Producer
from src.buses.events.in_memory_event_bus import in_memory_event_bus
from src.buses.events.topics import topics


@injectable(singleton=True)  # type: ignore
class InMemoryEventBusProducer(Producer):
    def publish(self, event: Event) -> None:
        aggregate_root = event.__class__.get_aggregate_root()
        topic = topics.get(aggregate_root)
        if topic is None:
            raise NotImplementedError(
                f"InMemoryEventBusProducer: No topic found for this aggregate root {aggregate_root}"
            )
        in_memory_event_bus.publish(topic, event)
