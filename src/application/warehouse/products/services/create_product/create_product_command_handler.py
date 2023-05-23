from uuid import UUID
from injectable import injectable, autowired, Autowired

from src.application.shared.commands.domain.command_handler import CommandHandler
from src.application.shared.events.ports.producer import Producer
from src.application.warehouse.products.domain.product import ProductFactory
from src.application.warehouse.products.services.create_product.create_product_command import (
    CreateProductCommand,
)
from src.application.warehouse.products.ports.product_respository import (
    ProductRepository,
)

AutowiredProducer = Autowired(Producer)
AutowiredProductRepository = Autowired(ProductRepository)


@injectable(singleton=True)  # type: ignore
class CreateProductCommandHandler(CommandHandler[CreateProductCommand, UUID]):
    @autowired
    def __init__(
        self,
        producer: AutowiredProducer,
        product_repository: AutowiredProductRepository,
    ) -> None:
        self._producer = producer
        self._product_repository = product_repository

    def handle(self, command: CreateProductCommand) -> UUID:
        product, event = ProductFactory.create(command.stock)
        self._producer.publish("product", event)
        self._product_repository.save(product)
        return product.uuid
