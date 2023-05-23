from injectable import injectable

from src.application.shared.events.domain.event import Event
from src.application.shared.events.ports.producer import Producer
from src.buses.events.in_memory_event_bus import in_memory_bus


@injectable(singleton=True)  # type: ignore
class InMemoryBusProducer(Producer):
    def publish(self, topic: str, event: Event) -> None:
        in_memory_bus.publish(topic, event)
