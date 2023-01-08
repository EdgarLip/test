import json
import pprint

full_key_path = ''
found_key = False

def read_json(file_name):
    with open(file_name, 'r') as json_file:
        json_data = json.load(json_file)
        return json_data

def check_if_key_exists(dict1, searched_key, current_path):

    if not isinstance(dict1, dict):
        return None
    if not dict1.keys():
        return None
    if searched_key in dict1:
        return searched_key

    for key_name in dict1.keys():
        local_found_key = check_if_key_exists(dict1[key_name], searched_key, '{}->{}'.format(current_path, key_name))

        if local_found_key:
            current_path = '{}->{}->{}'.format(current_path, key_name, local_found_key)
            print(current_path)
            break


if '__main__' == __name__:
    json_data = read_json('../databases/simple_dict.json')
    check_if_key_exists(dict1=json_data, searched_key='private_vlan', current_path='')
