import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = os.path.join(BASE_PATH, 'assets')

def get_asset_resource_path(asset_name):
    return os.path.join(ASSETS_PATH, asset_name)

class LoadAssets():
    def __init__(self) -> None:
        pass