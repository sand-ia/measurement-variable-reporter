from abc import ABC, abstractmethod
from typing import Union

from src.application.shared.commands.domain.command import Command


class CommandBus(ABC):
    # * When implementing, register all the query handlers in the constructor.

    @abstractmethod
    def dispatch(self, command: Command) -> Union[str, None]:
        raise NotImplementedError
