from dataclasses import dataclass

from src.shared.entities.domain.projection import Projection


@dataclass
class ProductCurrentState(Projection):
    name: str
    stock: int
