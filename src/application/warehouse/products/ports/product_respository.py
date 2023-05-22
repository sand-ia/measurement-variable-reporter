from abc import ABC

from src.application.shared.repositories.ports.repository import Repository
from src.application.warehouse.products.domain.product import Product


class ProductRepository(Repository[Product], ABC):
    pass
