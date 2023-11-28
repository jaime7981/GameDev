import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = os.path.join(BASE_PATH, 'assets')

def split_folders(path):
    final_path = ASSETS_PATH
    splited_path = path.split('/')

    for i in splited_path:
        final_path = os.path.join(final_path, i)

    return final_path

def get_asset_resource_path(asset_name):
    return os.path.join(ASSETS_PATH, split_folders(asset_name))

class LoadAssets():
    def __init__(self) -> None:
        pass