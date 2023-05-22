from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Union
from uuid import UUID

from src.application.shared.commands.domain.command import Command

C = TypeVar("C", bound=Command)
R = TypeVar("R", bound=Union[UUID, None])


class CommandHandler(Generic[C, R], ABC):
    @abstractmethod
    def handle(self, command: C) -> R:
        raise NotImplementedError
