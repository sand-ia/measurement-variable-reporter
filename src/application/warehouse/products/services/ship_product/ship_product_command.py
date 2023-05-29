from dataclasses import dataclass
from uuid import UUID
from src.application.shared.commands.domain.command import Command


@dataclass
class ShipProductCommand(Command):
    uuid: UUID
    amount: int