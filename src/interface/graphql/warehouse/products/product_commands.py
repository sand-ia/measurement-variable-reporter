from typing import Type, TypeAlias
from uuid import UUID
from injectable import autowired, Autowired
from graphene import (
    ObjectType,
    InputObjectType,
    ID,
    Int,
    Field,
    ResolveInfo,
)

from src.application.shared.commands.ports.command_bus import CommandBus
from src.application.warehouse.products.services.create_product.create_product_command import (
    CreateProductCommand,
)

DefaultCommandBus: TypeAlias = CommandBus
AutowiredCommandBus: Type[DefaultCommandBus] = Autowired(DefaultCommandBus)  # type: ignore


class CreateProductInput(InputObjectType):
    stock = Int()


class CreateProductOutput(ID):
    pass


class ProductCommands(ObjectType):
    create_product = Field(CreateProductOutput, product=CreateProductInput())

    @staticmethod
    @autowired
    def resolve_create_product(
        _parent: None,
        _info: ResolveInfo,
        product: CreateProductInput,
        command_bus: AutowiredCommandBus,
    ) -> UUID:
        create_product_command = CreateProductCommand(product.stock)
        uuid = command_bus.dispatch(create_product_command)
        if not isinstance(uuid, UUID):
            raise Exception
        return uuid


# TODO: Handle General Exception
