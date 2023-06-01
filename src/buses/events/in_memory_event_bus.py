import json
from threading import Thread
from typing import Any, Callable, Dict, List, TypeAlias
from uuid import uuid4


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

    def publish(self, topic: str, event: str) -> None:
        self.auth()
        file_path = f"src/buses/events/storage/{topic}.json"
        try:
            with open(file_path, "r", encoding="utf8") as file:
                data: List[Dict[str, Any]] = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        event_dict: Dict[str, Any] = json.loads(event)
        event_uuid = event_dict.get("uuid")
        if event_uuid is None:
            event_dict["uuid"] = str(uuid4())

        data.append(event_dict)

        with open(file_path, mode="w", encoding="utf8") as file:
            json.dump(data, file, indent=2)

        callbacks = self._callbacks_by_topic.get(topic)
        if callbacks is None:
            return
        for callback in callbacks:
            Thread(target=callback, args=(event,)).start()


# TODO: Get user and pass from .env
in_memory_event_bus = InMemoryEventBus("sandia", "sandia")
