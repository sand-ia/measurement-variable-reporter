from src.shared.entities.domain.bounded_context import BoundedContext
from src.shared.entities.domain.aggregate_root import (
    AggregateRoot,
    set_bounded_context,
)


class Warehouse(BoundedContext):
    pass


@set_bounded_context(Warehouse)
class WarehouseAggregateRoot(AggregateRoot):
    pass
