from injectable import injectable

from src.application.shared.events.domain.event import Event
from src.application.shared.events.ports.producer import Producer
from src.buses.events.in_memory_event_bus import in_memory_bus
from src.buses.events.topics import TOPIC


@injectable(singleton=True)  # type: ignore
class InMemoryEventBusProducer(Producer):
    def publish(self, event: Event) -> None:
        aggregate = event.__class__.get_aggregate()
        bounded_context = aggregate.get_bounded_context()
        bounded_context_topics = TOPIC.get(bounded_context)
        if bounded_context_topics is None:
            raise NotImplementedError(
                f"InMemoryEventBusProducer: No topics found for this bounded context {bounded_context}"
            )

        topic = bounded_context_topics.get(aggregate)
        if topic is None:
            raise NotImplementedError(
                f"InMemoryEventBusProducer: No topic found for this aggregate {aggregate}"
            )

        in_memory_bus.publish(topic, event)
