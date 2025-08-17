from src.core.env import environment


def get_workspaces_route():
    return environment.get_rest_baseurl() + "/workspaces"