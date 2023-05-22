"""
This type stub file was generated by pyright.
"""

from .objecttype import ObjectType, ObjectTypeOptions
from .interface import Interface
from .argument import Argument
from typing import Callable, Dict, Iterable, Type

MYPY = ...
if MYPY:
    ...
class MutationOptions(ObjectTypeOptions):
    arguments: Dict[str, Argument] = ...
    output: Type[ObjectType] = ...
    resolver: Callable = ...
    interfaces: Iterable[Type[Interface]] = ...


class Mutation(ObjectType):
    """
    Object Type Definition (mutation field)

    Mutation is a convenience type that helps us build a Field which takes Arguments and returns a
    mutation Output ObjectType.

    .. code:: python

        from graphene import Mutation, ObjectType, String, Boolean, Field

        class CreatePerson(Mutation):
            class Arguments:
                name = String()

            ok = Boolean()
            person = Field(Person)

            def mutate(parent, info, name):
                person = Person(name=name)
                ok = True
                return CreatePerson(person=person, ok=ok)

        class Mutation(ObjectType):
            create_person = CreatePerson.Field()

    Meta class options (optional):
        output (graphene.ObjectType): Or ``Output`` inner class with attributes on Mutation class.
            Or attributes from Mutation class. Fields which can be returned from this mutation
            field.
        resolver (Callable resolver method): Or ``mutate`` method on Mutation class. Perform data
            change and return output.
        arguments (Dict[str, graphene.Argument]): Or ``Arguments`` inner class with attributes on
            Mutation class. Arguments to use for the mutation Field.
        name (str): Name of the GraphQL type (must be unique in schema). Defaults to class
            name.
        description (str): Description of the GraphQL type in the schema. Defaults to class
            docstring.
        interfaces (Iterable[graphene.Interface]): GraphQL interfaces to extend with the payload
            object. All fields from interface will be included in this object's schema.
        fields (Dict[str, graphene.Field]): Dictionary of field name to Field. Not recommended to
            use (prefer class attributes or ``Meta.output``).
    """
    @classmethod
    def __init_subclass_with_meta__(cls, interfaces=..., resolver=..., output=..., arguments=..., _meta=..., **options): # -> None:
        ...
    
    @classmethod
    def Field(cls, name=..., description=..., deprecation_reason=..., required=...): # -> Field:
        """Mount instance of mutation Field."""
        ...
    

