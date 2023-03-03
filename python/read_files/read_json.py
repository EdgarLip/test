import json

def read_json(file_name):
    with open(file_name, 'r') as json_file:
        json_data = json.load(json_file)
        return json_data
