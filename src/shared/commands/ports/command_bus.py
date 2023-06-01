from abc import ABC, abstractmethod
from uuid import UUID

from src.shared.commands.domain.command import Command


class CommandBus(ABC):
    # * When implementing, register all the query handlers in the constructor.

    @abstractmethod
    def dispatch(self, command: Command) -> UUID | None:
        raise NotImplementedError