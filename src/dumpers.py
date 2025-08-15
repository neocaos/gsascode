

import json
import os

import yaml

from src.env import environment



def dump_file(folder: str,filename: str,info: dict):
    format = environment.get_format()
    if format == 'yaml':
        return dump_yaml_file(folder,filename,info)
    
    return dump_json_file(folder,filename,info)

def dump_yaml_file(folder: str,filename: str,info: dict):
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
    target_path = os.path.join(folder,f'{filename}.yaml')
    with open(target_path,'w+') as target_file:
        yaml.dump(info,target_file)

def dump_json_file(folder: str,filename: str,info: dict):
    
    target_path = os.path.join(folder,f'{filename}.json')
    with open(target_path,'w+') as target_file:
        json.dump(info,target_file,indent=4)
    