"""
This type stub file was generated by pyright.
"""

from graphql.type.typemap import GraphQLTypeMap

def is_graphene_type(_type): # -> Literal[True] | None:
    ...

def resolve_type(resolve_type_func, map, type_name, root, info): # -> type:
    ...

def is_type_of_from_possible_types(possible_types, root, info): # -> bool:
    ...

class TypeMap(GraphQLTypeMap):
    def __init__(self, types, auto_camelcase=..., schema=...) -> None:
        ...
    
    def reducer(self, map, type):
        ...
    
    def graphene_reducer(self, map, type):
        ...
    
    def construct_scalar(self, map, type): # -> GraphQLScalarType | GrapheneScalarType:
        ...
    
    def construct_enum(self, map, type): # -> GrapheneEnumType:
        ...
    
    def construct_objecttype(self, map, type): # -> GrapheneGraphQLType | GrapheneObjectType:
        ...
    
    def construct_interface(self, map, type): # -> GrapheneInterfaceType:
        ...
    
    def construct_inputobjecttype(self, map, type): # -> GrapheneInputObjectType:
        ...
    
    def construct_union(self, map, type): # -> GrapheneUnionType:
        ...
    
    def get_name(self, name):
        ...
    
    def construct_fields_for_type(self, map, type, is_input_type=...): # -> OrderedDict[Unknown, Unknown]:
        ...
    
    def get_resolver_for_type(self, type, name, default_value): # -> Any | partial[Unknown | Any | None] | None:
        ...
    
    def get_field_type(self, map, type): # -> GraphQLList | GraphQLNonNull:
        ...
    

