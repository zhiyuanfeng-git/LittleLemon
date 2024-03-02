from os.path import dirname,join
from json import load as sys_load_json

def get_file_full_path(file_name):
    """Get the full path of a given file"""
    module_dir = dirname(__file__)
    return join(module_dir,file_name)

def load_json(file_stream):
    return sys_load_json(file_stream)