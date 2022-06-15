
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
    with open(filename + ".json", encoding="utf-8") as file:
        return json.load(file)


def save_json(data, filename: str) -> None:
    with open(filename + ".json", 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4)  # sort_keys=True ensure_ascii=False


### CSV FUNCTIONS ###
import csv

def load_csv(filename: str):
    csv_return = list()
    with open(filename + ".csv") as file:
        list(map(
            lambda x: csv_return.append(x), csv.reader(file)))


def save_csv(data, filename: str) -> None:
    pass
