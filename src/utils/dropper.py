import json
import os

import yaml

from src.core.env import environment

format = environment.get_format()


def drop_file(folder: str, filename: str):
    path = os.path.join(folder, filename + f".{format}")
    try:
        if os.path.exists(path):
            os.remove(path)
        else:
            raise FileNotFoundError(f"File not found: {path}")
    except FileNotFoundError:
        pass

    except Exception as e:
        print("ERR!", str(e))
