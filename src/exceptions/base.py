from src.core.env import environment


class GSASCodeException(Exception):
    """Default exception for GSASCode errors."""

    def __init__(self, message):
        super().__init__(message)

    def __repr__(self) -> str:
        return f"<GsAsCodeException>"


class UnreachableGeoserver(GSASCodeException):

    def __init__(self):

        instance_url = environment.get_config_key("baseurl")

        super().__init__(f"Instance {instance_url} is unreachable")
