from typing import Dict, List, Type, TypeAlias
from inspect import signature
from uuid import UUID
from injectable import Autowired, autowired, injectable

from src.application.shared.commands.domain.command import Command
from src.application.shared.commands.ports.command_bus import CommandBus
from src.application.shared.commands.domain.command_handler import CommandHandler

DefaultCommandHandler: TypeAlias = CommandHandler[Command, UUID | None]
CommandHandlers: TypeAlias = List[DefaultCommandHandler]
AutowiredCommandHandlers: Type[CommandHandlers] = Autowired(CommandHandlers)  # type: ignore


@injectable(singleton=True)  # type: ignore
class InMemoryCommandBus(CommandBus):
    @autowired
    def __init__(self, command_handlers: AutowiredCommandHandlers) -> None:
        self.command_handlers: Dict[type, DefaultCommandHandler] = {}
        for command_handler in command_handlers:
            handle = command_handler.handle
            parameters = signature(handle).parameters.values()
            parameter = list(parameters)[0]
            command_class = parameter.annotation
            self.command_handlers[command_class] = command_handler

    def dispatch(self, command: Command) -> UUID | None:
        command_class = command.__class__
        handler = self.command_handlers.get(command_class)
        if handler is None:
            # TODO: raise correct exception.
            raise Exception("No handler registered")
        return handler.handle(command)
