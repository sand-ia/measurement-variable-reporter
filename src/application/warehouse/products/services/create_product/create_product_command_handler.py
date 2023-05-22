from injectable import injectable, autowired, Autowired

from src.application.shared.commands.domain.command_handler import CommandHandler
from src.application.warehouse.products.domain.product import ProductFactory
from src.application.warehouse.products.services.create_product.create_product_command import (
    CreateProductCommand,
)
from src.application.warehouse.products.ports.product_respository import (
    ProductRepository,
)

AutowiredProductRepository = Autowired(ProductRepository)


@injectable(singleton=True)  # type: ignore
class CreateProductCommandHandler(CommandHandler[CreateProductCommand, str]):
    @autowired
    def __init__(self, product_repository: AutowiredProductRepository) -> None:
        self._product_repository = product_repository

    def handle(self, command: CreateProductCommand) -> str:
        product, event = ProductFactory.create(command.stock)
        return product.uuid
