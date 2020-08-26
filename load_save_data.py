
### YAML FUNCTIONS ###
import yaml


def load_yml(filename: str):
    with open(filename + ".yaml") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def save_yml(data, filename: str) -> None:
    with open(r'{}.yaml'.format(filename), 'w') as file:
        yaml.dump(data, file)


### JSON FUNCTIONS ###
import json


def load_json(filename: str):
    with open(filename + ".json") as file:
        return json.load(file)


def save_json(data, filename: str) -> None:
    with open(filename + ".json", 'w') as file:
        json.dump(data, file, indent=4)  # sort_keys=True ensure_ascii=False
