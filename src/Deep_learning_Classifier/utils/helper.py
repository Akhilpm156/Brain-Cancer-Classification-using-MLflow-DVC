import os
from box.exceptions import BoxValueError
import yaml
from Deep_learning_Classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import Box
from pathlib import Path
import base64

@ensure_annotations
def read_yaml(path_to_yaml:Path)-> Box:
    """reads yaml file and return config box type"""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml_file: {path_to_yaml} loaded successfully")
            return Box(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """Create list of directories"""
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """ save json data """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at : {path}")
      
