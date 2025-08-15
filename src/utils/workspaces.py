import json
import os
from src.dumpers import dump_file, dump_yaml_file
from src.env import environment
import requests

from src.types.modes import Mode

AUTH_HEADER = environment.get_config_key('auth_header')

workspaces_dir = os.path.join(environment.get_files_dir(),'workspaces')

if not os.path.exists(workspaces_dir):
    os.mkdir(workspaces_dir)


def get_workspaces_route():
    return environment.get_rest_baseurl() + "/workspaces"

def dump_single_workspace(workspace, workspaces_dir):
    href = workspace['href']
    response = requests.get(href,headers=dict(authorization=AUTH_HEADER))
    ws_detail = response.json()['workspace']
    
    final_dict = dict(
        workspace= ws_detail
    )
    
    print(final_dict)
    dump_file(folder=workspaces_dir,filename=workspace['name'],info=final_dict)
    
    

def dump_workspaces():
    workspaces_route = get_workspaces_route()
    
    response = requests.get(workspaces_route,headers=dict(authorization= AUTH_HEADER))
    workspaces = response.json()['workspaces']
    
    
    dump_file(workspaces_dir,'__list',workspaces)
            
    for workspace in workspaces['workspace']:
        dump_single_workspace(workspace,workspaces_dir)
        
    
    


# BASE_URL = environment.__dict__['gs_baseurl']


def handle_workspaces(mode: Mode):
    
    if mode == Mode.DUMP:
        dump_workspaces()
    
    
