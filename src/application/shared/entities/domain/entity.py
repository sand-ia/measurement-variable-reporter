from uuid import UUID


class Entity:
    def __init__(self, uuid: UUID) -> None:
        self.uuid = uuid
