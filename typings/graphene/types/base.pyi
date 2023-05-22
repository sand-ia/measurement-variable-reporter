"""
This type stub file was generated by pyright.
"""

import six
from ..utils.subclass_with_meta import SubclassWithMeta

if six.PY3:
    ...
class BaseOptions:
    name: str = ...
    description: str = ...
    _frozen: bool = ...
    def __init__(self, class_type) -> None:
        ...
    
    def freeze(self): # -> None:
        ...
    
    def __setattr__(self, name, value): # -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class BaseType(SubclassWithMeta):
    @classmethod
    def create_type(cls, class_name, **options): # -> Any:
        ...
    
    @classmethod
    def __init_subclass_with_meta__(cls, name=..., description=..., _meta=..., **_kwargs): # -> None:
        ...
    


