"""
This type stub file was generated by pyright.
"""

def import_string(dotted_path, dotted_attributes=...): # -> Any:
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. When a dotted attribute path is also provided, the
    dotted attribute path would be applied to the attribute/class retrieved from
    the first step, and return the corresponding value designated by the
    attribute path. Raise ImportError if the import failed.
    """
    ...

def lazy_import(dotted_path, dotted_attributes=...): # -> partial[Any]:
    ...

