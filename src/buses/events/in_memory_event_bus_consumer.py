from typing import List, TypeAlias, Type
from injectable import autowired, Autowired

from src.application.shared.events.domain.event_handler import EventHandler
from src.buses.events.topics import topics
from src.buses.events.in_memory_event_bus import in_memory_event_bus

DefaultEventHandler: TypeAlias = EventHandler
EventHandlers: TypeAlias = List[DefaultEventHandler]
AutowiredEventHandlers: Type[EventHandlers] = Autowired(EventHandlers)  # type: ignore


class InMemoryEventBusConsumer:
    @autowired
    def __init__(self, event_handlers: AutowiredEventHandlers) -> None:
        for event_handler in event_handlers:
            aggregate_root = event_handler.__class__.get_aggregate_root()
            topic = topics.get(aggregate_root)
            if topic is not None:
                handle = event_handler.handle
                in_memory_event_bus.subscribe(topic, handle)
