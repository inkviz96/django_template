import os
from dataclasses import dataclass
from typing import List

import yaml
from marshmallow_dataclass import class_schema


@dataclass
class Config:
    django_static_url: str
    django_secret_key: str
    django_allowed_hosts: List[str]


config_path = "/../config.yaml"

with open(os.path.dirname(__file__) + config_path) as f:
    config_data = yaml.safe_load(f)

config: Config = class_schema(Config)().load(config_data)
