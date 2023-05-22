"""
This type stub file was generated by pyright.
"""

from .scalars import Scalar

class UUID(Scalar):
    """
    Leverages the internal Python implmeentation of UUID (uuid.UUID) to provide native UUID objects
    in fields, resolvers and input.
    """
    @staticmethod
    def serialize(uuid): # -> str:
        ...
    
    @staticmethod
    def parse_literal(node): # -> UUID | None:
        ...
    
    @staticmethod
    def parse_value(value): # -> UUID:
        ...
    


