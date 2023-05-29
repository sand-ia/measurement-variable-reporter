from typing import Type, TypeAlias
from uuid import UUID
from injectable import autowired, Autowired
from graphene import (
    ObjectType,
    InputObjectType,
    ID,
    Int,
    String,
    Boolean,
    Field,
    ResolveInfo,
)

from src.application.shared.commands.ports.command_bus import CommandBus
from src.application.warehouse.products.services.create_product.create_product_command import (
    CreateProductCommand,
)
from src.application.warehouse.products.services.ship_product.ship_product_command import (
    ShipProductCommand,
)

DefaultCommandBus: TypeAlias = CommandBus
AutowiredCommandBus: Type[DefaultCommandBus] = Autowired(DefaultCommandBus)  # type: ignore


class CreateProductInput(InputObjectType):
    name = String()
    stock = Int()


class ProductCommands(ObjectType):
    create_product = Field(ID, product=CreateProductInput())
    ship_product = Field(Boolean, uuid=ID(), amount=Int())

    @staticmethod
    @autowired
    def resolve_create_product(
        _parent: None,
        _info: ResolveInfo,
        product: CreateProductInput,
        command_bus: AutowiredCommandBus,
    ) -> UUID:
        create_product_command = CreateProductCommand(product.name, product.stock)
        uuid = command_bus.dispatch(create_product_command)
        if not isinstance(uuid, UUID):
            raise Exception
        return uuid

    @staticmethod
    @autowired
    def resolve_ship_product(
        _parent: None,
        _info: ResolveInfo,
        uuid: UUID,
        amount: int,
        command_bus: AutowiredCommandBus,
    ) -> bool:
        ship_product_command = ShipProductCommand(uuid, amount)
        command_bus.dispatch(ship_product_command)
        return True


# TODO: Handle General Exception
