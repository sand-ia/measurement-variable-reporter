from typing import Any
from injectable import injectable
from src.application.shared.events.ports.producer import Producer

from src.buses.events.in_memory_event_bus import in_memory_bus


@injectable(singleton=True)  # type: ignore
class InMemoryBusProducer(Producer[Any]):
    # TOPIC: str = "topic"

    def publish(self, topic: str, message: Any) -> None:
        in_memory_bus.publish(topic, message)
