from typing import Callable, Type, TypeVar
from src.application.shared.entities.domain.bounded_context import BoundedContext
from src.application.shared.entities.domain.entity import Entity


class AggregateRoot(Entity):
    @staticmethod
    def get_bounded_context() -> Type[BoundedContext]:
        return BoundedContext


T = TypeVar("T", bound=Type[AggregateRoot])


def set_bounded_context(bounded_context: Type[BoundedContext]) -> Callable[[T], T]:
    def decorator(cls: T) -> T:
        def get_bounded_context():
            return bounded_context

        cls.get_bounded_context = get_bounded_context
        return cls

    return decorator
