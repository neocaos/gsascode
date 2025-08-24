import json
import os
from src.utils.dropper import drop_file
from src.utils.dumpers import dump_file, dump_yaml_file
from src.core.env import environment
from src.core.routes import get_workspaces_route
import requests

from src.types.modes import Mode
from src.utils.decorators import check_reachability
from src.utils.loaders import load_file

from deepdiff import DeepDiff


#region CONSTANTS & MAGIC NUMBERS

AUTH_HEADER = environment.get_config_key("auth_header")
workspaces_dir = os.path.join(environment.get_files_dir(), "workspaces")
workspaces_route = get_workspaces_route()
change_keys = ["values_changed"
                   , "type_changes"]

#endregion

if not os.path.exists(workspaces_dir):
    os.mkdir(workspaces_dir)


def dump_single_workspace(workspace, workspaces_dir):
    href = workspace["href"]
    response = requests.get(href, headers=dict(authorization=AUTH_HEADER))
    ws_detail = response.json()["workspace"]

    final_dict = dict(workspace=ws_detail)

    print(final_dict)
    dump_file(folder=workspaces_dir, filename=workspace["name"], info=final_dict)


def dump_workspaces():

    response = requests.get(workspaces_route, headers=dict(authorization=AUTH_HEADER))
    workspaces = response.json()["workspaces"]

    dump_file(workspaces_dir, "__list", workspaces)

    for workspace in workspaces["workspace"]:
        dump_single_workspace(workspace, workspaces_dir)


def read_local_workspaces(deep: bool = False):
    return load_file(workspaces_dir, "__list")


def read_remote_workspaces():
    response = requests.get(workspaces_route, headers=dict(authorization=AUTH_HEADER))
    return response.json()["workspaces"]


# BASE_URL = self.get_config_key("baseurl")
@check_reachability()
def compare_workspaces(deep: bool = False):

    local_workspaces_dict = read_local_workspaces()
    remote_workspaces_dict = read_remote_workspaces()
    diff = DeepDiff(local_workspaces_dict, remote_workspaces_dict)

    
    has_changes = diff and any(key in change_keys for key in diff.keys())

    json_diff = diff.to_json()
    
    safe_dict = json.loads(json_diff)

    if has_changes:
        dump_file(workspaces_dir, "diff", safe_dict)
    else:
        drop_file(workspaces_dir, "diff",safe_dict)

    pass



@check_reachability()
def apply_workspaces():
    
    diff_file = load_file(workspaces_dir,'diff')
    print("DF =>",diff_file)


@check_reachability()
def handle_workspaces(mode: Mode):
    if mode == Mode.DUMP:
        dump_workspaces()
    elif mode == Mode.PLAN:
        return compare_workspaces()
    elif mode == Mode.APPLY:
        return apply_workspaces()
