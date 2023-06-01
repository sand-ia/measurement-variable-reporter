from typing import Type, TypeAlias
from uuid import UUID
from injectable import injectable, autowired, Autowired

from src.application.shared.commands.domain.command_handler import CommandHandler
from src.application.shared.events.ports.producer import Producer
from src.application.warehouse.products.domain.product import ProductFactory
from src.application.warehouse.products.services.create_product.create_product_command import (
    CreateProductCommand,
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
class CreateProductCommandHandler(CommandHandler[CreateProductCommand, UUID]):
    @autowired
    def __init__(
        self,
        producer: AutowiredProducer,
        product_query_repository: AutowiredProductQueryRepository,
    ) -> None:
        self._producer = producer
        self._product_query_repository = product_query_repository

    def handle(self, command: CreateProductCommand) -> UUID:
        product, event = ProductFactory.create(command.name, command.stock)
        self._producer.publish(event)
        return product.uuid
