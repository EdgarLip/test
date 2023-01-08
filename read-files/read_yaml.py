
import yaml

def open_yaml(file_name):
    with open(file_name) as f:
        yaml_data = yaml.load(f, yaml.BaseLoader)
        return yaml_data