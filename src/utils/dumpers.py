import json
import os

import yaml

from src.core.env import environment

format = environment.get_format()


def dump_file(folder: str, filename: str, info: dict):
    """
    Dumps the provided information to a file in the specified folder and filename.
    The output format is determined by the current environment settings and can be either YAML or JSON.
    Args:
        folder (str): The directory where the file will be saved.
        filename (str): The name of the file to write.
        info (dict): The data to be dumped into the file.
    Returns:
        Any: The result of the dump operation, as returned by the underlying format-specific function.
    Raises:
        Exception: If the format is not supported or if the dump operation fails.
    """

    if format == "yaml":
        return dump_yaml_file(folder, filename, info)

    return dump_json_file(folder, filename, info)


def dump_yaml_file(folder: str, filename: str, info: dict):
    """
    Writes the provided dictionary to a YAML file in the specified folder.

    Args:
        folder (str): The directory where the YAML file will be saved.
        filename (str): The name of the YAML file (without extension).
        info (dict): The dictionary containing data to be dumped into the YAML file.

    Returns:
        None

    Raises:
        OSError: If the file cannot be created or written to.
        yaml.YAMLError: If the dictionary cannot be serialized to YAML.
    """
    target_path = os.path.join(folder, f"{filename}.yaml")
    with open(target_path, "w+") as target_file:
        yaml.dump(info, target_file)


def dump_json_file(folder: str, filename: str, info: dict):
    """
    Saves a dictionary as a JSON file in the specified folder with the given filename.
    Args:
        folder (str): The directory where the JSON file will be saved.
        filename (str): The name of the JSON file (without extension).
        info (dict): The dictionary data to be dumped into the JSON file.
    Returns:
        None
    Raises:
        OSError: If the file cannot be written due to an OS error.
        TypeError: If the info dictionary contains non-serializable objects.
    """

    target_path = os.path.join(folder, f"{filename}.json")
    with open(target_path, "w+") as target_file:
        json.dump(info, target_file, indent=4)
