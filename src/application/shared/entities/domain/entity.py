from uuid import UUID, uuid4


class Entity:
    def __init__(self, uuid: UUID | None = None) -> None:
        self.uuid = uuid if uuid is not None else uuid4()
