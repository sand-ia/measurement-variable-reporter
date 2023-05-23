from typing import Any
from injectable import injectable
from src.application.shared.events.ports.consumer import Consumer


from src.buses.events.in_memory_event_bus import Subscription, in_memory_bus


@injectable(singleton=True)  # type: ignore
class InMemoryBusConsumer(Consumer[Any]):
    # TODO: Can we use asyncio to handle async await

    def subscribe(self, topic: str, callback: Any) -> Any:
        subscription = in_memory_bus.subscribe(topic, callback)
        return subscription

    def subscribe_and_wait(self, topic: str) -> Any:
        promise: Any = None
        subscription: Subscription | None = None

        def complete_promise(response: Any) -> None:
            nonlocal promise
            promise = response
            if subscription is not None:
                subscription.unsubscribe()

        subscription = self.subscribe(topic, complete_promise)

        while True:
            if promise is not None:
                return promise
