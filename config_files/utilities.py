import json

def read_json(path: str) -> dict:
    """ Reads json files
    :param path: path to json file"""

    with open(path, 'r') as file:
        return json.load(file)

# print(read_json.__doc__)
