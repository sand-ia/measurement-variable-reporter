import json
from typing import Any, Dict
from uuid import UUID
from injectable import injectable

from src.application.warehouse.products.domain.product import Product
from src.infrastructure.consumers.warehouse.products.ports.product_command_repository import (
    ProductCommandRepository,
)
from src.infrastructure.repositories.in_memory_db import in_memory_db
from src.utils.json_encoder import Encoder


@injectable(singleton=True)  # type: ignore
class InMemoryDBProductCommandRepository(ProductCommandRepository):
    def save(self, entity: Product) -> None:
        entity_json: str = json.dumps(entity, cls=Encoder)
        in_memory_db.save("products", entity_json)

    def update(self, uuid: UUID, updates: Dict[str, Any]) -> None:
        updates_json: str = json.dumps(updates, cls=Encoder)
        in_memory_db.update("products", str(uuid), updates_json)

    def delete(self, uuid: UUID) -> None:
        raise NotImplementedError
