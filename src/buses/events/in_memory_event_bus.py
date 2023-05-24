from datetime import datetime
from enum import Enum
import json
from uuid import UUID
from threading import Thread
from typing import Any, Callable, Dict, List, TypeAlias
from inspect import isclass

from src.application.shared.events.domain.event import Event


class BusEvent:
    def __init__(self, event: Event) -> None:
        self.__dict__.update(event.__dict__)
        self.event = event.__class__


Callback: TypeAlias = Callable[[Any], None]
Callbacks: TypeAlias = List[Callback]


class Subscription:
    def __init__(self, callback: Callback | None, callbacks: Callbacks | None) -> None:
        self.callback = callback
        self.callbacks = callbacks

    def unsubscribe(self):
        if self.callback is None or self.callbacks is None:
            return
        self.callbacks.remove(self.callback)


class InMemoryEventBus:
    class Encoder(json.JSONEncoder):
        def default(self, o: Any):
            if isinstance(o, UUID):
                return str(o)
            if isinstance(o, datetime):
                return o.isoformat()
            if isinstance(o, Enum):
                return o.value
            if isclass(o):
                return o.__name__
            if o.__class__ is not None:
                return o.__dict__
            return super().default(o)

    def __init__(self, user: str, password: str) -> None:
        self._user: str = user
        self._password: str = password
        self._is_authorized: bool = False
        self._callbacks_by_topic: Dict[str, Callbacks] = {}

    def connect(self, user: str, password: str) -> None:
        if self._user == user and self._password == password:
            self._is_authorized = True
            return
        raise PermissionError("InMemoryEventBus: Unauthorazed Access")

    def auth(self):
        if self._is_authorized:
            return
        raise PermissionError("InMemoryEventBus: Unauthorazed Access")

    def subscribe(self, topic: str, callback: Callback) -> Subscription:
        self.auth()
        callbacks = self._callbacks_by_topic.get(topic)
        if callbacks is None:
            callbacks = []
            self._callbacks_by_topic[topic] = callbacks
        callbacks.append(callback)
        subscription = Subscription(callback, callbacks)
        return subscription

    def publish(self, topic: str, event: BusEvent) -> None:
        self.auth()

        file_path = f"src/buses/events/storage/{topic}.json"

        data: List[Any]

        try:
            with open(file_path, "r", encoding="utf8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(event)

        with open(file_path, mode="w", encoding="utf8") as file:
            json.dump(data, file, indent=2, cls=InMemoryEventBus.Encoder)

        callbacks = self._callbacks_by_topic.get(topic)
        if callbacks is None:
            return
        for callback in callbacks:
            Thread(target=callback, args=(event,)).start()


# TODO: Get user and pass from .env
in_memory_event_bus = InMemoryEventBus("sandia", "sandia")
