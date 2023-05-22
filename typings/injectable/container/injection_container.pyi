"""
This type stub file was generated by pyright.
"""

from typing import Dict, Optional, Set
from injectable.container.namespace import Namespace

class InjectionContainer:
    """
    InjectionContainer globally manages injection namespaces and the respective
    injectables registries.

    This class shouldn't be used directly and will be removed from the injectable's
    public API in the future.

    Invoking :func:`load_injection_container` is the only necessary action before
    injecting dependencies. Attempting to call an autowired function before invoking
    :func:`load_injection_container` will log a warning indicating that the injection
    container is empty.

    This class is not meant to be instantiated and will raise an error if instantiation
    is attempted.

    .. deprecated:: 3.4.0
        This class will be removed from the public API in the future.
    """
    LOADING_DEFAULT_NAMESPACE: Optional[str] = ...
    LOADING_FILEPATH: Optional[str] = ...
    LOADED_FILEPATHS: Set[str] = ...
    NAMESPACES: Dict[str, Namespace] = ...
    def __new__(cls):
        ...
    
    @classmethod
    def load(cls, search_path: str = ..., *, default_namespace: str = ...): # -> None:
        """
        Loads injectables under the search path to the :class:`InjectionContainer`
        under the designated namespaces.

        :param search_path: (optional) path under which to search for injectables. Can
                be either a relative or absolute path. Defaults to the caller's file
                directory.
        :param default_namespace: (optional) designated namespace for registering
                injectables which does not explicitly request to be addressed in a
                specific namespace. Defaults to
                :const:`injectable.constants.DEFAULT_NAMESPACE`.

        Usage::

          >>> from injectable import InjectionContainer
          >>> InjectionContainer.load()

        .. note::

            This method will not scan any file more than once regardless of being
            called successively. Multiple invocations to different search paths will
            add found injectables to the :class:`InjectionContainer` without clearing
            previously found ones.

        .. deprecated:: 3.4.0
            This method will be removed from the public API in the future. Use
            :func:`load_injection_container` instead.
        """
        ...
    
    @classmethod
    def load_dependencies_from(cls, absolute_search_path: str, default_namespace: str, encoding: str = ...): # -> None:
        ...
    


