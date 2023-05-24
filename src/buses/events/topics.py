from typing import Dict, Type, TypeVar

from src.application.shared.entities.domain.aggregate_root import AggregateRoot


ORGANISATION = "sandia"
SERVICE = "demo"


def _topic_generator(aggregate_root: Type[AggregateRoot]):
    return (
        f"{ORGANISATION}.{SERVICE}."
        f"{aggregate_root.get_bounded_context().__name__.lower()}."
        f"{aggregate_root.__name__.lower()}"
    )


TOPIC: Dict[Type[AggregateRoot], str] = {}

T = TypeVar("T", bound=Type[AggregateRoot])


def topify(aggregate_root: T) -> T:
    TOPIC[aggregate_root] = _topic_generator(aggregate_root)
    return aggregate_root
