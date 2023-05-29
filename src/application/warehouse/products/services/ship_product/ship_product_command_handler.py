from typing import Type, TypeAlias
from uuid import UUID
from injectable import injectable, autowired, Autowired

from src.application.shared.commands.domain.command_handler import CommandHandler
from src.application.shared.events.ports.producer import Producer
from src.application.warehouse.products.services.ship_product.ship_product_command import (
    ShipProductCommand,
)
from src.application.warehouse.products.ports.product_respository import (
    ProductRepository,
)

DefaultProducer: TypeAlias = Producer
AutowiredProducer: Type[DefaultProducer] = Autowired(DefaultProducer)  # type: ignore

DefaultProductRepository: TypeAlias = ProductRepository
AutowiredProductRepository: Type[DefaultProductRepository] = Autowired(
    DefaultProductRepository
)  # type: ignore


@injectable(singleton=True)  # type: ignore
class ShipProductCommandHandler(CommandHandler[ShipProductCommand, UUID]):
    @autowired
    def __init__(
        self,
        producer: AutowiredProducer,
        product_repository: AutowiredProductRepository,
    ) -> None:
        self._producer = producer
        self._product_repository = product_repository

    def handle(self, command: ShipProductCommand) -> UUID:
        product = self._product_repository.get(command.uuid)
        event = product.ship(command.amount)
        self._product_repository.update(product)
        self._producer.publish(event)
        return product.uuid