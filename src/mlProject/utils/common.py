import os
from box.exceptions import BoxValueError
import yaml
from src.mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    Reads the yaml file and returns the config box
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
        '''
        Creates list of directories
        
        '''
        
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created : {path}")
                


@ensure_annotations
def save_json(path:Path,data:dict):
    """
    Saves the json file
    """
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    logger.info(f"Json file successfully saved to : {path}")                
            


@ensure_annotations            
def load_json(path:Path) -> ConfigBox:
    
    """
    Loads the json file and returns the config box
    """
    with open(path) as json_file:
            content = json.load(json_file)
    logger.info(f"Json file successfully loaded from : {path}") 
    return ConfigBox(content)


@ensure_annotations           
def save_bin(data : Any,path:Path):
    '''
    save Binary file
    
    ''' 
    joblib.dump(value=data,filename=path)  
    logger.info(f"binary file successfully saved at : {path}") 
    

@ensure_annotations
def load_bin(path:Path) -> Any:
    '''
    load Binary file
    
    '''  
    data = joblib.load(path)
    logger.info(f"binary file successfully loaded from : {path}")
    return data
   
    
@ensure_annotations       
def get_size(path:Path)-> str:
    '''
    get size in kb
    
    '''
    
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"    
    
        
            
            
            
            
            
            
        
        
        
        
        
        
        
        