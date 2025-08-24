import json
from src.core.env import environment
import yaml
import os

format = environment.get_format()


def find_and_read_yaml_file(folder, filename):
    file_path = os.path.join(folder, filename + ".yaml")
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    return data


def find_and_read_json_file(folder, name):
    file_path = os.path.join(folder, name + ".json")
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


def load_file(folder, name):

    if format == "yaml":
        return find_and_read_yaml_file(folder, name)

    return find_and_read_json_file(folder, name)
