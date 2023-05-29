from typing import List
from uuid import UUID
from injectable import injectable

from src.application.warehouse.products.domain.product import Product
from src.application.warehouse.products.ports.product_respository import (
    ProductRepository,
)
from src.infrastructure.repositories.in_memory_db import in_memory_db


@injectable(singleton=True)  # type: ignore
class InMemoryDBProductRepository(ProductRepository):
    def save(self, entity: Product) -> None:
        in_memory_db.save("products", entity.__dict__)

    def get(self, uuid: UUID) -> Product:
        document = in_memory_db.get("products", str(uuid))
        product = Product(document["name"], document["stock"], UUID(document["uuid"]))
        return product

    def update(self, entity: Product) -> None:
        in_memory_db.update("products", entity.__dict__)

    def delete(self, uuid: UUID) -> None:
        raise NotImplementedError

    def find(self, uuids: List[UUID] | None = None) -> List[Product]:
        raise NotImplementedError
