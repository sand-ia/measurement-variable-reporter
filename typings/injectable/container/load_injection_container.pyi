"""
This type stub file was generated by pyright.
"""

def load_injection_container(search_path: str = ..., *, default_namespace: str = ..., encoding: str = ...) -> None:
    """
    Loads injectables under the search path to a shared injection container under the
    designated namespaces.

    :param search_path: (optional) path under which to search for injectables. Can
            be either a relative or absolute path. Defaults to the caller's file
            directory.
    :param default_namespace: (optional) designated namespace for registering
            injectables which does not explicitly request to be addressed in a
            specific namespace. Defaults to
            :const:`injectable.constants.DEFAULT_NAMESPACE`.
    :param encoding: (optional) defines which encoding to use when reading project files
            to discover and register injectables. Defaults to ``utf-8``.

    Usage::

      >>> from injectable import load_injection_container
      >>> load_injection_container()

    .. note::

        This method will not scan any file already scanned by previous calls to it.
        Multiple invocations to different search paths will add found injectables into
        the injection container without clearing previously loaded ones but never
        loading a same injectable more than once.

    .. versionadded:: 3.4.0
    """
    ...

