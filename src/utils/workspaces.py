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

AUTH_HEADER = environment.get_config_key("auth_header")

workspaces_dir = os.path.join(environment.get_files_dir(), "workspaces")
workspaces_route = get_workspaces_route()

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
    return load_file(workspaces_dir,"__list")
    
    
    
    



def read_remote_workspaces():
    response = requests.get(workspaces_route, headers=dict(authorization=AUTH_HEADER))
    return response.json()["workspaces"]
    

# BASE_URL = environment.__dict__['gs_baseurl']
@check_reachability()
def compare_workspaces(deep: bool= False):
    
    local_workspaces_dict = read_local_workspaces()
    remote_workspaces_dict = read_remote_workspaces()
    print("LOCAL =>", local_workspaces_dict)
    print("REMOTE =>",remote_workspaces_dict)
    diff = DeepDiff(local_workspaces_dict,remote_workspaces_dict)
    print("DIff => ",diff)
    
    if diff and diff['values_changed']:
        dump_file(workspaces_dir,'diff',diff)
    else:
        drop_file(workspaces_dir,'diff')
        
    
    
    
    pass

@check_reachability()
def handle_workspaces(mode: Mode):
    if mode == Mode.DUMP:
        dump_workspaces()
        
    elif mode == Mode.PLAN:
        return compare_workspaces()
