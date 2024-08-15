 
# Config Reader - YAML ----------------------------------------------
# This module reads YAML files and returns the data as a dictionary.
# This service can be used to read configuration files in YAML format.
# For Python only.
# ------------------------------------------------------------------
import yaml

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data
