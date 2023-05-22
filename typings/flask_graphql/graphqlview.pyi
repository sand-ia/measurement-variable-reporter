"""
This type stub file was generated by pyright.
"""

from flask.views import View

class GraphQLView(View):
    schema = ...
    executor = ...
    root_value = ...
    pretty = ...
    graphiql = ...
    backend = ...
    graphiql_version = ...
    graphiql_template = ...
    graphiql_html_title = ...
    middleware = ...
    batch = ...
    methods = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def get_root_value(self): # -> None:
        ...
    
    def get_context(self): # -> Request:
        ...
    
    def get_middleware(self): # -> None:
        ...
    
    def get_backend(self): # -> None:
        ...
    
    def get_executor(self): # -> None:
        ...
    
    def render_graphiql(self, params, result): # -> str:
        ...
    
    format_error = ...
    encode = ...
    def dispatch_request(self): # -> str | Response:
        ...
    
    def parse_body(self): # -> dict[str, str] | ImmutableMultiDict[str, str] | dict[Unknown, Unknown]:
        ...
    
    def should_display_graphiql(self): # -> bool:
        ...
    
    def request_wants_html(self): # -> bool:
        ...
    

