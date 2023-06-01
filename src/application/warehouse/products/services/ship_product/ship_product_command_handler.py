from typing import Type, TypeAlias
from uuid import UUID
from injectable import injectable, autowired, Autowired

from src.application.shared.commands.domain.command_handler import CommandHandler
from src.application.shared.events.ports.producer import Producer
from src.application.warehouse.products.services.ship_product.ship_product_command import (
    ShipProductCommand,
)
from src.application.warehouse.products.ports.product_query_respository import (
    ProductQueryRepository,
)

DefaultProducer: TypeAlias = Producer
AutowiredProducer: Type[DefaultProducer] = Autowired(DefaultProducer)  # type: ignore

DefaultProductQueryRepository: TypeAlias = ProductQueryRepository
AutowiredProductQueryRepository: Type[DefaultProductQueryRepository] = Autowired(
    DefaultProductQueryRepository
)  # type: ignore


@injectable(singleton=True)  # type: ignore
class ShipProductCommandHandler(CommandHandler[ShipProductCommand, None]):
    @autowired
    def __init__(
        self,
        producer: AutowiredProducer,
        product_query_repository: AutowiredProductQueryRepository,
    ) -> None:
        self._producer = producer
        self._product_query_repository = product_query_repository

    def handle(self, command: ShipProductCommand) -> None:
        product = self._product_query_repository.get(command.uuid)
        event = product.ship(command.amount)
        self._producer.publish(event)
