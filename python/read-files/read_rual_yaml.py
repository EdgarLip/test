from ruamel.yaml import YAML

def test_yaml_db(file_name):
    with open(file_name) as yaml_file:
        yaml = YAML(typ="safe")
        yaml_data = yaml.load(yaml_file)
        return yaml_data