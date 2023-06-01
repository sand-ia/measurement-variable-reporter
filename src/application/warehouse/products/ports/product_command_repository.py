from src.shared.repositories.ports.command_repository import CommandRepository
from src.application.warehouse.products.projections.product_current_state import (
    ProductCurrentState,
)


class ProductCommandRepository(CommandRepository[ProductCurrentState]):
    pass
