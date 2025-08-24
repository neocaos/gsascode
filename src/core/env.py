import os
import json
import requests
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

REQUIRED_ARGS = []


class Env(object):

    __target_config_dir = os.path.join(os.getcwd(), ".gsascode")
    __target_config_files_dir = os.path.join(__target_config_dir, "files")
    __target_config_file = os.path.join(__target_config_dir, "config.yml")

    def get_env_file(self):

        return self.__target_config_file

    def get_env_dir(self):
        return self.__target_config_dir

    def get_files_dir(self):
        return self.__target_config_files_dir

    def set_config(self):

        self.__target_config_dir = os.path.join(os.getcwd(), ".gsascode")
        if not os.path.exists(self.__target_config_dir):
            os.mkdir(self.__target_config_dir)

        if not os.path.exists(self.__target_config_files_dir):
            os.mkdir(self.__target_config_files_dir)

        self.__target_config_file = os.path.join(self.__target_config_dir, "config.yml")

        if not os.path.exists(self.__target_config_file):
            with open(self.__target_config_file, "w") as f:
                yaml.dump({"path": f"{self.__target_config_file}"}, f)

    def get_format(self):
        return self.get_config_key("format")

    def __init__(self):

        for x in REQUIRED_ARGS:
            value = os.getenv(x, None)
            if not value:
                raise Exception(f"Env Variable {x} isn't set.")

            self.__dict__[x] = value

        self.set_config()
        config_file = self.__target_config_file

        with open(config_file, "r") as f:
            try:
                my_dict = json.load(f)
            except json.JSONDecodeError:
                my_dict = {}

    def persist(self, key, value):

        current_config = self.__get_config()

        new_config = current_config | {key: value}
        self.__set_config(new_config)

    def get_web_baseurl(self):
        return self.get_config_key("baseurl") + "/geoserver/web/?0"

    def __set_config(self, config_dict):
        with open(self.__target_config_file, "w") as f:
            yaml.dump(config_dict, f)

    def __get_config(self):

        with open(self.__target_config_file, "r") as file:
            return yaml.load(file, Loader)

    def is_initialized(self):
        config = self.__get_config()
        return config is not None and config["baseurl"] is not None

    def is_authenticated(self):
        config = self.__get_config()
        return config is not None and config["auth_header"] is not None

    def is_reachable(self):

        if not self.is_initialized() or not self.is_authenticated():
            return False
        url = self.get_web_baseurl()
        response = requests.get(url, timeout=(5, None))

        return response and response.status_code == 200

    def get_config_key(self, key: str):
        return dict(self.__get_config()).get(key, None)

    def get_rest_baseurl(self):
        return self.get_config_key("baseurl") + "/geoserver/rest"


environment = Env()
