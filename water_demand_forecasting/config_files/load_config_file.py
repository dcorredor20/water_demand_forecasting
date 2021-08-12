"""Load config file."""
from typing import Dict
import yaml


def load_config_file(path: str) -> Dict:
    with open(path, "r") as in_file:
        config = yaml.safe_load(in_file)
        return config
