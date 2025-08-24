from src.core.env import environment
from src.exceptions.base import UnreachableGeoserver


def check_reachability():

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Code to perform before calling the original function
            if not environment.is_reachable():
                raise UnreachableGeoserver

            return func(*args, **kwargs)

        return wrapper

    return decorator
