from src.infrastructure.consumers.ports.command_repository import CommandRepository
from src.application.warehouse.products.domain.product import Product


class ProductCommandRepository(CommandRepository[Product]):
    pass
