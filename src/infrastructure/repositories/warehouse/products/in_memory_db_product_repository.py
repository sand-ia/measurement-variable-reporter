from typing import Any, Dict, List, Union
from injectable import injectable

from src.application.warehouse.products.domain.product import Product
from src.application.warehouse.products.ports.product_respository import (
    ProductRepository,
)
from src.infrastructure.repositories.in_memory_db import in_memory_db


@injectable(singleton=True)  # type: ignore
class InMemoryDBProductRepository(ProductRepository):
    def save(self, entity: Product) -> None:
        document: Dict[str, Any] = {
            "uuid": entity.uuid,
            "stock": entity.stock,
        }
        in_memory_db.save("products", document)

    def get(self, uuid: str) -> Product:
        document = in_memory_db.get("products", uuid)
        product = Product(document["uuid"], document["stock"])
        return product

    def update(self, uuid: str, entity: Product) -> None:
        raise NotImplementedError

    def delete(self, uuid: str) -> None:
        raise NotImplementedError

    def find(self, uuids: Union[List[str], None] = None) -> List[Product]:
        raise NotImplementedError
