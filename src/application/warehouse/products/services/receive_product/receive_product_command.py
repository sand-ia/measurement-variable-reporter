from dataclasses import dataclass
from uuid import UUID
from src.shared.commands.domain.command import Command


@dataclass
class ReceiveProductCommand(Command):
    uuid: UUID
    amount: int
