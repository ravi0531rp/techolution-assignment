import json
import os
from constants import SAVE_ASSETS_ROOT

def save_data(data, filename):
    """
    Save data to a JSON file.
    
    Args:
        data: The data to be saved.
        filename: The name of the JSON file.
    """
    with open(os.path.join(SAVE_ASSETS_ROOT, filename), 'w') as file:
        json.dump(data, file, indent=4)

def load_data(filename):
    """
    Load data from a JSON file.
    
    Args:
        filename: The name of the JSON file.
    
    Returns:
        The loaded data.
    """
    if os.path.exists(os.path.join(SAVE_ASSETS_ROOT, filename)):
        with open(os.path.join(SAVE_ASSETS_ROOT, filename), 'r') as file:
            return json.load(file)
    else:
        return []
