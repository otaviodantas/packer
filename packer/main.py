import yaml
import subprocess

from packer import ROOT_PATH


def __load_manifest_file(path: str):
    with open(path, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    file = __load_manifest_file(ROOT_PATH / 'manifest.yaml')
    print(file)
