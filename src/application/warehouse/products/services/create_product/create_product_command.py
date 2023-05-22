from dataclasses import dataclass
from src.application.shared.commands.domain.command import Command


@dataclass
class CreateProductCommand(Command):
    stock: int
